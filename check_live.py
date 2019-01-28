import requests
import re


class SendGet:
    def __init__(self, url_list):
        self.url_list = url_list

    def send_request(self, site, address=''):
        try:
            headers = {
                'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            }
            response = requests.request("GET", site + address, headers=headers, timeout=15)
            return response
        except Exception:
            return 0


    def request_url(self, site, address=''):
        if address == '':
            return self.send_request(site, address)
        if address != '':
            return self.send_request(site, address)


    def send_request_one_site(self, url, data_version=None):
        response = self.request_url(url)
        if response == 0:
            return url + ' ATENTION SOMTHING HAPPEND EEEEEEEEEERRRRRRRRRRRRRRRRRRRROOOOORRRRRRRR'
        response_code = response.status_code
        response_text = response.text
        pattern = '\d{1,2}\w{2,3}\d{4}-\w{1,25}-v[\d.]{1,12}'
        result = re.search(pattern, response_text)
        if result == None:
            return 'Invalid data version   ' + url[8:-2].split('.')[0] + '   ' + str(response_code)
        else:
            if response_code != 200: return url[8:-2].split('.')[0] + '   ' + response_code + '     EEEEEEEEEERRRRRRRRRRRRRRRRRRRROOOOORRRRRRRR'
            if response_code == 200 and data_version is None: return result.group(0) + '   ' + url[8:-2].split('.')[0] + '   ' + str(response_code)
            else:
                if result.group(0) == data_version: return url[8:-2].split('.')[0] + '  ' + data_version + ' == ' + result.group(0) + ' OK!!!'
                else: return url[8:-2].split('.')[0] + '  ' + data_version + ' != ' + result.group(0) + ' UPDATE VERSION PLEASE!!!'


    def check_sitemap(self, url, sitemap):
        response = self.request_url(url, sitemap)
        if response.status_code != 200: return 'WEBSITE  ' + url[8:-2].split('.')[0] + '  Sitemap does not answer'
        #pattern = 'https://\S{,60}\.\w{2,15}/[-/\w\d/_]*'
        pattern = 'https://\S{,60}\.\w{1,15}[/]*[-/\w\d/_]*'
        sitemap_list = re.findall(pattern, response.text)
        for page in sitemap_list:
            try:
                status_code = self.send_request(page).status_code
                if status_code != 200:
                    yield 'WEB SITE   ' + url[8:-1] + '     ' + page[8:] + ' DOES NOT ANSWER'
            except:
                yield 'WEB SITE   ' + url[8:-1] + '     ' + page[8:] + ' DOES NOT ANSWER'
            if page == sitemap_list[-1]:
                yield url[8:-1] + ' Finished ' + str(len(sitemap_list)) + ' urls on sitemap'


    def sub_check_sitemap(self):
        pass

                    #return data_version + ' != ' + result + ' UPDATE VERSION PLEASE!!!'
 #pattern = '\d{1,2}\w{2,3}\d{4}-\w{1,25}-v[\d]{1,12}'