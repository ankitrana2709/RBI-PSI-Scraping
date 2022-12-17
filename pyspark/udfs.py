#spark = SparkSession.builder.appName('spark_app').getOrCreate()

def get_english_name(species):
    return species.split("(")[0].strip()


def get_start_year(period):
    return int(period.split("-")[0].split("(")[1].strip())


def get_trend(annual_percentage_change):
    annual_percentage_change = float(annual_percentage_change)
    if annual_percentage_change < -3.00:
        return 'strong decline'
    if annual_percentage_change >= -3.00 and annual_percentage_change <= -0.50 :
        return 'weak decline'
    if annual_percentage_change > -0.50 and annual_percentage_change < 0.50 :
        return 'no change'
    if annual_percentage_change >= 0.50 and annual_percentage_change <= 3.00 :
        return 'weak increase'
    if annual_percentage_change > 3.00:
        return 'strong increase'

#spark.udf.register(name='total_salary', f=total_salary, returnType=IntegerType())
print(get_trend(-3.02))