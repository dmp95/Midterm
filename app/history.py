import os
import pandas as pd
from decimal import Decimal
from .functions_defination import add, subtract, multiply, divide, exponent
from .calculation import Calculation

class Calculations:

    history_dir = "data"
    history_file = os.path.join(history_dir, "calculation_history.csv")
    history = pd.DataFrame(columns=["Operation", "Operand_A", "Operand_B", "Result"])

    @staticmethod
    def create_empty_history():
        return pd.DataFrame(columns=["Operation", "Operand_A", "Operand_B", "Result"])
   
    @staticmethod
    def load_history():
     
        print(f"Attempting to load history from {Calculations.history_file}")
        if os.path.exists(Calculations.history_file) and os.path.getsize(Calculations.history_file) > 0:
            with open(Calculations.history_file, 'r') as file:
                file_contents = file.read()
            Calculations.history = pd.read_csv(Calculations.history_file)
        else:
            Calculations.history = Calculations.create_empty_history()

    @staticmethod
    def save_history():
        os.makedirs(Calculations.history_dir, exist_ok=True)
        Calculations.history.to_csv(Calculations.history_file, index=False)
        with open(Calculations.history_file, 'r') as file:
            file_contents = file.read()

    @staticmethod
    def add_calculation(calculation: Calculation):
        result = calculation.perform_operation()
        new_entry = {
            'Operation': calculation.operation.__name__,
            'Operand_A': float(calculation.a),
            'Operand_B': float(calculation.b),
            'Result': float(result)
        }
     
        Calculations.load_history()      
        new_entry_df = pd.DataFrame([new_entry])

        if not Calculations.history.empty:
            Calculations.history = pd.concat([Calculations.history, new_entry_df], ignore_index=True)
        else:
            Calculations.history = new_entry_df
       
        Calculations.save_history()


    @staticmethod
    def clear_history():
        Calculations.history = Calculations.create_empty_history()
        Calculations.save_history()

    @staticmethod
    def delete_history():
        try:
            os.remove(Calculations.history_file)
            print(f"Deleted file: {Calculations.history_file}")
        except FileNotFoundError:
            print(f"No history found")

    @staticmethod
    def view_history():
        Calculations.load_history()
        return Calculations.history

    @staticmethod
    def get_latest():
       
        Calculations.load_history()
        if not Calculations.history.empty:
            latest_entry = Calculations.history.iloc[-1]
            operation_map = {
                'add': add,
                'subtract': subtract,
                'multiply': multiply,
                'divide': divide,
                'exponent': exponent
            }
            operation = operation_map.get(latest_entry['Operation'])
            if operation is None:
                raise ValueError(f"Unknown operation '{latest_entry['Operation']}' in history")
            return Calculation(operation, Decimal(latest_entry['Operand_A']), Decimal(latest_entry['Operand_B']))
        else:
            return None

    @staticmethod
    def delete_history_entry(index: int):
        Calculations.load_history()
        if 0 <= index < len(Calculations.history):
            Calculations.history = Calculations.history.drop(index).reset_index(drop=True)
            Calculations.save_history()
        else:
            print(f"Index {index} is out of range. No entry deleted.")

    @staticmethod
    def save_history_to_csv(file_path: str):
        print(f"Saving history to {file_path}")
        Calculations.load_history()
        Calculations.history.to_csv(file_path, index=False)
        print(f"History saved to {file_path}")

    @staticmethod
    def load_history_from_csv(file_path: str = "data/calculation_history.csv"):
        try:
            Calculations.history = pd.read_csv(file_path)
        except FileNotFoundError:
            Calculations.history = Calculations.create_empty_history()
