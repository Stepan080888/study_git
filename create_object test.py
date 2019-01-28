from check_live import SendGet
from data_sites import site_list

prod_list = [i for i in site_list if i[-10:] != '.db.rv.ua/']
stage_list = [i for i in site_list if i[-10:] == '.db.rv.ua/']

send_get = SendGet(stage_list)
#k = send_get.send_requests_all_sites()
#print(k)

for i in prod_list:
    k = send_get.send_request_one_site(i)
    print(k)
