
from __init__ import *
from model import *
from userDefinedExceptions import NotFound

'''Important data'''
target_products_translated = {
    "ind_cco_fin_ult1": "Current Accounts",
    "ind_cder_fin_ult1": "Derivada Account",
    "ind_cno_fin_ult1": "Payroll Account",
    "ind_ctju_fin_ult1": "Junior Account",
    "ind_ctma_fin_ult1": "Más Particular Account",
    "ind_ctop_fin_ult1": "Particular Account",
    "ind_ctpp_fin_ult1": "Particular Plus Account",
    "ind_deco_fin_ult1": "Short-term deposits",
    "ind_deme_fin_ult1": "Medium-term deposits",
    "ind_dela_fin_ult1": "Long-term deposits",
    "ind_ecue_fin_ult1": "E-Account",
    "ind_fond_fin_ult1": "Funds",
    "ind_hip_fin_ult1": "Mortgage",
    "ind_plan_fin_ult1": "Pensions",
    "ind_pres_fin_ult1": "Loans",
    "ind_reca_fin_ult1": "Taxes",
    "ind_tjcr_fin_ult1": "Credit Card",
    "ind_valo_fin_ult1": "Securities",
    "ind_viv_fin_ult1": "Home Account",
    "ind_nomina_ult1": "Payroll",
    "ind_nom_pens_ult1": "Pensions",
    "ind_recibo_ult1": "Direct Debit"
}

""" Template for dummy data for a user"""
user_data =     {
"fecha_dato": "2016-06-28",
"ncodpers": "15889",
"ind_empleado": "F",
'pais_residencia':'LV' ,
"sexo":'V',
'age': None,
"fecha_alta":"1995-15-01",
"ind_nuevo":"0",
"antiguedad":None,
"indrel":"1",
"ult_fec_cli_1t":"",
"indrel_1mes":"1",
"tiprel_1mes":"A",
"indresi":"S",
"indext":"N",
"conyuemp":"N",
"canal_entrada":"KAT",
"indfall":"N",
"tipodom":"1",
"cod_prov":"28",
"nomprov":"MADRID",
"ind_actividad_cliente":None,
'renta':None,
"segmento":None
}

@api.route('/recommend', methods = ['POST', 'GET'])
class recommend(Resource):
    recommend_post_data = api.model ("registerAdminData",{'seniority':fields.String(),'income':fields.String(),\
        'age':fields.String(), 'segment': fields.String() , \
            'client_activity': fields.String()})
    @api.doc(body=recommend_post_data)
    def post(self):
        """
        -- API description: This API is used to recommend product to users based on some entered data
        -- params: seniority', 'gender', 'nationality', 'age','rel_type','activity_type','segment'
        -- return data: msg, status and repsonse_data
        """
        msg = None
        status = None
        response_data = None
        try:
            # getting the data from the request
            data = request.json            

            ''' Map activity type to Active (1) or inactive (0)'''
            user_activity = data['client_activity']
            user_segment = data['segment']
            if (user_activity == "ACTIVE"):
                user_activity = '1'
            elif user_activity == "INACTIVE":
                user_activity = '0'
            else:
                msg = "User Activity type not found"
                status = "Failed"
                response_data = None
                raise NotFound
            
            if (user_segment == 'INDIVIDUAL'):
                user_segment = '02 - PARTICULARES'
            elif (user_segment == 'UNIVERSITY'):
                user_segment = '03 - UNIVERSITARIO'
            elif user_segment == 'TOP':
                user_segment = '01 - TOP'
            else:
                msg = "User segment not found"
                status = "Failed"
                response_data = None
                raise NotFound
                            
            
            user_data['age'] = data['age']
            user_data['antiguedad'] =  data['seniority']
            user_data['ind_actividad_cliente'] = user_activity
            user_data['renta'] = data['income']
            user_data['segmento'] = user_segment
    
            print(user_data)
            '''
            generating the recommendations from the model
            feeding our client's data to the model to get the predictions
            '''
            x_vars_list, y_vars_list, cust_dict = processData([user_data], {}, False)
            test_X = np.array(x_vars_list)
            xgtest = xgb.DMatrix(test_X)
            predictions = recommend_model.predict(xgtest)
            predictions = np.argsort(predictions,axis=1)
            predictions = np.fliplr(predictions)[:,:7]
            final_preds = ["".join(list(target_cols[pred])) for pred in predictions[0]]
            
            ''' Print the recommended products translated in english'''
            target_cols_translated = []
            for i in final_preds:
                target_cols_translated.append(target_products_translated[i])
            
            return jsonify({
                'msg': 'Recommendations for user generated successfully',
                'status': 'Success',
                'response_data':{'Recommended Products':target_cols_translated} 
            })
        except NotFound as e:
            print('Exception',e)
            return jsonify({
                'msg': msg,
                'status': status,
                'response_data':None    
            })
            
        except KeyError as e:
            # if one of the parameters not provided by the user
            print('Exception',e)
            return jsonify({
                'msg': 'Missing field',
                'status': 'Failed',
                'response_data':None    
            })

if __name__ == '__main__':
    # Load "model.pkl"
    recommend_model = joblib.load('model.pkl') 
    # run app 
    app.run(debug=True, host='0.0.0.0')