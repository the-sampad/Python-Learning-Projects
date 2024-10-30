# I tried Different methods to scrap. Even after using anaconda, venv it didn't work. Also I used bs4, lxml but failed eacvh time.
# Even I thought of using scrapy but I moved on to next day project. I decided to try later.
# 
# According to me it will be better to use API of Amazon. Actually it is the best way.
# 
# 
# import smtplib
# import requests
# import scrapy

# username = 'sampadedge@gmail.com'
# pass_ = 'Munna@2018'
# connection = smtplib.SMTP('smtp.gmail.com', 587)
# connection.starttls()
# connection.login(user=username, password=pass_)
# # connection.sendmail(
# #     from_addr=username,
# #     to=pass_,
# #     msg = 
# # )
# url_link = 'https://www.amazon.in/Zebronics-ZEB-NC3300-Powered-Laptop-Cooling/dp/B07YWS9SP9/?_encoding=UTF8&pd_rd_w=MFcax&content-id=amzn1.sym.841d8717-36ee-4e1e-b23c-37287c297234&pf_rd_p=841d8717-36ee-4e1e-b23c-37287c297234&pf_rd_r=435RE6DS9CPPZYCSSEZ3&pd_rd_wg=FHZa3&pd_rd_r=3045aaa5-37cd-498d-9fc3-31f262e6d16a&ref_=pd_gw_cr_cartx'

# response = requests.get(url=url_link)
# data = response.content

# path = '//*[@id="corePrice_feature_div"]/div/span/span[2]/span[2]'

# source_code = html.fromstring(data)

# tree = source_code.xpath(path)

# print(tree)