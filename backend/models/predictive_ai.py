from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

from utils.data_loader import loan_loader


class PredictiveAI:

    def __init__(self):

        df = loan_loader.load_data().copy()

        self.categorical = [
            "Region",
            "Product",
            "Customer_Type"
        ]

        self.numeric = [
            "Loan_Amount",
            "Property_Value",
            "Bureau_Score",
            "FOIR_%"
        ]

        self.features = self.categorical + self.numeric

        self.encoders = {}

        for col in self.categorical:
            encoder = LabelEncoder()
            df[col] = encoder.fit_transform(df[col].astype(str))
            self.encoders[col] = encoder

        target = LabelEncoder()
        df["Decision"] = target.fit_transform(df["Decision"])
        self.target = target

        X = df[self.features]
        y = df["Decision"]

        self.model = RandomForestClassifier(
            n_estimators=100,
            random_state=42
        )

        self.model.fit(X, y)

    def predict(self, data):

        row = []

        for col in self.categorical:
            row.append(
                self.encoders[col].transform([data[col]])[0]
            )

        row.extend([
            float(data["Loan_Amount"]),
            float(data["Property_Value"]),
            int(data["Bureau_Score"]),
            float(data["FOIR_"])
        ])

        prediction = self.model.predict([row])[0]

        return self.target.inverse_transform([prediction])[0]


predictor = PredictiveAI()