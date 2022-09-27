import pickle , numpy as np
class prediction1():

    def __init__ (self,data):
        self.data = data
    def model_load(self):
        with open (r'artifacts/model.pkl','rb') as file:
            self.model = pickle.load(file)
    def output(self):
        self.model_load()
        x_feature = np.array(self.model.feature_names_in_)
        user_input_array = np.zeros(338)
        user_input= self.data['state']
        if user_input =='WB':
            user_input_array[0]= 0
        if user_input=='BH':
            user_input_array[0]=1    
        if user_input =='OR':
            user_input_array[0]=2    
        if user_input =='AS':
            user_input_array[0]=3
        if user_input =='MZ':
            user_input_array[0]=4
        if user_input=='ML':
            user_input_array[0]=5
        if user_input =='SK':
            user_input_array[0]=6
        if user_input=='TR':
            user_input_array[0]=7
        if user_input =='NL':
            user_input_array[0]=8

        user_input_array[1] = self.data["Adhoc count_oct'21"]
        input_report_ceneter = self.data['Reporting Center']
        concat_report_cenetr = 'Reporting Center_'+ input_report_ceneter
        index = np.where(x_feature == concat_report_cenetr)[0][0]
        user_input_array[index]=1

        input_report_ceneter = self.data['Actual vehicle type']
        concat_actual_vehicle_type = 'Actual vehicle type_'+input_report_ceneter
        print(concat_actual_vehicle_type)
        index1 = np.where(x_feature == concat_actual_vehicle_type)[0][0]
        user_input_array[index1]=1

        print(user_input_array)
        result = {'Additonal Adhoc Vehicle Required':self.model.predict([user_input_array])[0]}
        

        return result