import pandas as pd
from flask_restful import Resource


class PandasTestResource(Resource):
    def get(self):
        print ('1')
        num_list = [[1,2,3,4,5],[6,7,8,9,0]]
        df = pd.DataFrame(num_list)
        df = df.to_json()
        print (df)

        return df