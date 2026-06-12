import pandas as pd

def export_excel(
data,
filename
):

    df = pd.DataFrame(data)

    filepath = f"""
    generated_reports/
    {filename}.xlsx
    """

    df.to_excel(
    filepath,
    index=False
    )

    return filepath