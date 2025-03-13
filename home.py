from data_loading import Create_dataframe
import logs.log_fn as log
data_path='Data/Rider-Info.csv'
try:
    food_delivery=Create_dataframe(data_path,True)
    food_delivery.show()


    food_delivery.printSchema()
    print('---Dataframe created successfully---')
    print('***********************')
    # logging.basicConfig(filename='logs/loginfo.log',level=logging.INFO,format='%(asctime)s ,%(levelname)s,'
    #                                                                           '%(message)s')#log file created
    # # warnings,critical,info,debug,error--levels
    # logging.info('Data frame created successfully')
    log.log_Info(f'Data frame created successfully')
except Exception as e:
    print(f'There is some error while creating table:{e}')
    print('**************************')
    # logging.basicConfig(filename='logs/loginfo.log', level=logging.ERROR())  # log file created
    # # warnings,critical,info,debug,error--levels
    # logging.error(f'There is some error while creating table:{e}')
    log.log_Error(f'There is some error while creating table:{e}')
print('******************Analytics1****************************')
from Analytics.file1 import Peak_Hours

try:
    result = Peak_Hours(food_delivery)
    result.show()
    result.write.csv('Result/Analytics1',header=True,mode="overwrite")
    log.log_Info('Analytics1 executed and result generated')
except Exception as e:
    log.log_Error(e)