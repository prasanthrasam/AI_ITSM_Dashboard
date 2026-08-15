import pandas as pd


class ExcelService:

    def __init__(self):
        self.df = None

    def load_excel(self, uploaded_file):
        """
        Load uploaded Excel file into DataFrame
        """
        self.df = pd.read_excel(uploaded_file)
        return self.df

    def get_dataframe(self):
        return self.df

    def get_summary(self):

        if self.df is None:
            return None

        summary = {
            "rows": len(self.df),
            "columns": len(self.df.columns),
            "missing": int(self.df.isnull().sum().sum()),
            "column_names": self.df.columns.tolist()
        }

        return summary

    def get_datatypes(self):

        if self.df is None:
            return None

        datatype_df = self.df.dtypes.reset_index()
        datatype_df.columns = ["Column", "Datatype"]

        return datatype_df