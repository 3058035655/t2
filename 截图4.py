# -*- coding: utf8 -*-
import time
import xlrd
from selenium import webdriver
#
# def read_excel(filename):
#     data = xlrd.open_workbook(filename)  # 打开xls文件
#     sheet = data.sheets()[0]  # 打开第一张表
#     rows = sheet.nrows  # 获取表的行数
#     cols = sheet.ncols  # 获取表的列数
#     nrows = bytes(rows)
#     ncols = bytes(cols)
#     print("共:"+nrows+"行,  "+ncols+"列")
#     #for i in range(rows):
#     for i in range(3):
#         if i == 0:
#             continue
#         for j in range(cols - 1):
#             ctype = sheet.cell(i, j).ctype  # 表格的数据类型
#             cell = sheet.cell_value(i, j)
#             if ctype == 2 and cell % 1 == 0.0:  # ctype为2且为浮点
#                 cell = int(cell)  # 浮点转成整型
#             cell = bytes(cell)
#             url="这里我是利用excel中的ID拼接成的URL"
#             print(url)
#             url='https://www.hongkunjinfu.com/'
#             browser = webdriver.Firefox()
#             browser.set_window_size(1200, 900)
#             browser.get(url)  # Load page
#             time.sleep(10)
#             js = "var q=document.documentElement.scrollTop=10000"
#             browser.execute_script(js)
#             time.sleep(10)
#             browser.execute_script("""
#                     $('#main').siblings().remove();
#                     $('#aside__wrapper').siblings().remove();
#                     $('.ui.sticky').siblings().remove();
#                     $('.follow-me').siblings().remove();
#                     $('img.ui.image').siblings().remove();
#                     """)
#             browser.save_screenshot("图片保存路径\\图片名称.png")
#             browser.close()
# if __name__ == "__main__":
#
#     read_excel("excel的存放路径\\excel名称.xls")
url='https://www.hongkunjinfu.com/'
browser = webdriver.Firefox()
browser.set_window_size(1200, 900)
browser.get(url)  # Load page
time.sleep(3)
js = "var q=document.documentElement.scrollTop=10000"
browser.execute_script(js)
time.sleep(10)
# browser.execute_script("""
#         $('#main').siblings().remove();
#         $('#aside__wrapper').siblings().remove();
#         $('.ui.sticky').siblings().remove();
#         $('.follow-me').siblings().remove();
#         $('img.ui.image').siblings().remove();
#         """)
browser.execute_script("""$(document).ready(function() {                        	
                        	var searchVideo = true;                        
                        	$("#downloadForm").submit(function(event) {
                        		submitTheForm(event);
                        	});                        
                        	$("#downloadBtn1").click(function(event){
                        		submitTheForm(event);
                        	});                        
                        	function submitTheForm(event){                        
                        		event.preventDefault();                        
                        		var downloadUrl = document.forms["fd"]["video"].value;                        
                        		if (downloadUrl==null || downloadUrl==""){
                        		} else {
                        			if (searchVideo == true){
                        				var that = $("#loading-message");
                        				var that1 = $("#dlSection");
                        				var that2 = $("#footer");
                        				var that3 = $("#pageDesc");                        			  
                        				that.css('display', 'block');
                        				that2.css('display', 'none');
                        				that3.css('display', 'none');                        			  
                        				searchVideo = false;
										document.forms["fd"]["video"].value = encodeURI(downloadUrl);                        
                        				setTimeout(function(){
                        					$('#fd')[0].submit();
                        				}, 20);                        
                        				setTimeout(
                        					function() {
                        						searchVideo = true;
                        				}, 30000);
                        			} else {
                        			}
                        		}
                        	}
                        });    
""")
browser.save_screenshot("图片保存路径\\图片名称.png")
browser.close()