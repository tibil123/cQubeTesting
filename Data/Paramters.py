# import base64
# import os
# import time
#
# class Data():
#
#
#     #id's
#
#     login = "login"
#     email = "exampleInputEmail"
#     passwd = "exampleInputPassword"
#     new_pass = "newPasswd"
#     conf_pass = "cnfPasswd"
#     change_pass_btn = "btn"
#     homeicon = "home"
#     logout ="/html/body/app-root/app-home/mat-toolbar/button[2]/span"
#     fieldReq = "/html/body/app-root/app-login/div[1]/div[2]/div[2]/form/div[2]/div/label"
#     # username = base64.b64decode("username").decode("utf-8")
#     # password = base64.b64decode("password").decode("utf-8")
#     url = "https://cqube.tibilprojects.com/"
#     username ="radhika@cqube.com"
#     password = "tibil123"
#
#
#     loginbtn ="//button[@type='submit']"
#     # loginbtn ="login"
#
#
#     dots = "leaflet-interactive"
#     SAR_Details ="//div[@class='row']/div[@class='col-sm-4']/span"
#     hyper_link = "//p/span"
#     directory = "//p[contains(text(),' Semester report for:')]/span"
#     Download = "download"
#     value1 ="Ahmedabad"
#
#     # Dash board
#     Dashboard = "menu"
#     header = "//h4"
#     # school_infra_Report
#     # school_infra = "si"
#     infro_dist = "//select[@name='myDistrict']/option"
#     infro_block = "//select[@name='myBlock']/option"
#     infro_cluster ="//select[@name='myCluster']/option"
#
#     sel_districts ="//select[@name='myDistrict']/option"
#     sel_blocks ="//select[@name='myBlock']/option"
#     sel_clusters ="//select[@name='myCluster']/option"
#
#     sc_district = "//select[@name='myDistrict']/option[2]"
#     sc_block = "//select[@name='myBlock']/option[2]"
#     sc_cluster ="//select[@name='myCluster']/option[2]"
#
#
#
#     x_axis ="//select[@id='x_axis']/option"
#     x_Total_Schools = "//select[@id='x_axis']/option[2]"
#     x_Total_Data = "//select[@id='x_axis']/option[3]"
#     x_Average_parameters = "//select[@id='x_axis']/option[4]"
#     x_Handwash = "//select[@id='x_axis']/option[5]"
#     x_Solar_Panel = "//select[@id='x_axis']/option[6]"
#     x_Library = "//select[@id='x_axis']/option[7]"
#     x_Drinking_Water = "//select[@id='x_axis']/option[8]"
#     x_Tap_Water = "//select[@id='x_axis']/option[9]"
#     x_Hand_Pump = "//select[@id='x_axis']/option[10]"
#     x_PlayGround = "//select[@id='x_axis']/option[11]"
#     x_News_Paper = "//select[@id='x_axis']/option[12]"
#     x_Digital_Board = "//select[@id='x_axis']/option[13]"
#     x_Electricity = "//select[@id='x_axis']/option[14]"
#     x_Total_Toilets = "//select[@id='x_axis']/option[15]"
#     x_Boys_Toilet = "//select[@id='x_axis']/option[16]"
#     x_Girls_Toilet = "//select[@id='x_axis']/option[17]"
#     x_CWSN_Boys = "//select[@id='x_axis']/option[18]"
#     x_CWSN_Girls = "//select[@id='x_axis']/option[19]"
#     x_Boys_Urinals = "//select[@id='x_axis']/option[20]"
#     x_Girls_Urinals = "//select[@id='x_axis']/option[21]"
#     infra_hyperlink ="//p/span"
#     y_axis ="//select[@id='y_axis']/option"
#     y_Total_Schools = "//select[@id='y_axis']/option[2]"
#     y_Total_Data = "//select[@id='y_axis']/option[3]"
#     y_Average_parameters = "//select[@id='y_axis']/option[4]"
#     y_Handwash = "//select[@id='y_axis']/option[5]"
#     y_Solar_Panel = "//select[@id='y_axis']/option[6]"
#     y_Library = "//select[@id='y_axis']/option[7]"
#     y_Drinking_Water = "//select[@id='y_axis']/option[8]"
#     y_Tap_Water = "//select[@id='y_axis']/option[9]"
#     y_Hand_Pump = "//select[@id='y_axis']/option[10]"
#     y_PlayGround = "//select[@id='y_axis']/option[11]"
#     y_News_Paper = "//select[@id='y_axis']/option[12]"
#     y_Digital_Board = "//select[@id='y_axis']/option[13]"
#     y_Electricity = "//select[@id='y_axis']/option[14]"
#     y_Total_Toilets = "//select[@id='y_axis']/option[15]"
#     y_Boys_Toilet = "//select[@id='y_axis']/option[16]"
#     y_Girls_Toilet = "//select[@id='y_axis']/option[17]"
#     y_CWSN_Boys = "//select[@id='y_axis']/option[18]"
#     y_CWSN_Girls = "//select[@id='y_axis']/option[19]"
#     y_Boys_Urinals = "//select[@id='y_axis']/option[20]"
#     y_Girls_Urinals = "//select[@id='y_axis']/option[21]"
#
#     # sc_Reportmap
#     School_infra = "//*[@id='usr']/span/span[contains(text(),'School Infrastructure')]"
#     Reportmap = "//*[@id='crtUsr']/div/span[contains(text(),'Report(Map)')]"
#     Report = " //*[@id='chPass']/div/span[contains(text(),'Report')]"
#     scm_block = "block"
#     scm_cluster = "cluster"
#     scm_school = "school"
#     sc_choosedist = "//select[@id='choose_dist']/option"
#     sc_chooseblock = "//select[@id='choose_block']/option"
#     sc_choosecluster = "//select[@id='choose_cluster']/option"
#     sc_infrascores = "//select[@id='choose_infra']/option"
#     sc_no_of_schools = "schools"
#
#     scm_district = "//select[@id='choose_dist']/option[2]"
#     scm_blk = "//select[@id='choose_block']/option[2]"
#     scm_clust = "//select[@id='choose_cluster']/option[2]"
#
#     Dash_head ="//h4"
#     d_names = "//th[contains(text(),'district')]"
#     login_in = "//span[@class='span']"
#     SAR = "SAR"
#     Logout = "logout"
#     Home_icon = "//i[@id='home']"
#     select_district = 'myDistrict'
#     select_blocks = 'myBlock'
#     select_clusters = 'myCluster'
#     select_month = 'month'
#     select_year = 'year'
#     # login = "//button[@type='submit']"
#     select_sem_district = '/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]'
#     select_sem_blocks = '/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[2]'
#     select_sem_clusters = '/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[3]'
#
#     CRC_Districts = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-bar-chart/div/div[3]/div[2]/select[1]/option"
#     #User_option
#     user_options ="//button[@id='usr']/span/mat-icon"
#     u_create ="crtUsr"
#     p_change ="chPass"
#
#     No_schools = '/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-map-view/div/div[4]/div[2]'
#     No_sem_schools='/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[4]/div[2]'
#     SR_Blocks_btn = "block"
#     SR_Clusters_btn = "cluster"
#     SR_Schools_btn = "school"
#     Download_icon = "//i[@id='download']"
#     #user_creation
#     user ="/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav/div/mat-nav-list/mat-list/mat-list-item/div/button/span/mat-icon"
#     create_user ="/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav/div/mat-nav-list/mat-list/div/a[1]/div/span"
#     create_headtext ="//h2"
#     fname ="//input[@name='firstname']"
#     mname ="//input[@name='middlename']"
#     lname = "//input[@name='lastname']"
#     male ="//input[@name='gender'][1]"
#     female ="//input[@name='gender'][2]"
#     mail ="//input[@name='email']"
#     designation ="//input[@name='Designation']"
#     confpass ="//input[@name='cnfpass']"
#     rolesoptions ="//select/option"
#     admin ="//select/option[2]"
#     drc = "//select/option[3]"
#     drv = "//select/option[4]"
#     Adoc = "//select/option[5]"
#     Demission ="//select/option[6]"
#     changepwd = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav/div/mat-nav-list/mat-list/div/a[2]/div/span"
#     new_pwd ="//input[@name='newPasswd']"
#     conf_pwd ="//input[@name='cnfpass']"
#     submit = "//button[@type='submit']"
#     errormsg ="//p"
#
#     # for SAR_2
#     SAR_Blocks_btn = "block"
#     SAR_Clusters_btn = "cluster"
#     SAR_Schools_btn = "school"
#     # footer
#     schoolcount="schools"
#     students = "students"
#     DateRange = "dateRange"
#
#     SAR_Dnames = "//*[@id='choose_dist']/option"
#     SAR_Bnames = "//*[@id='choose_block']/option"
#     SAR_cnames = "//*[@id='choose_cluster']/option"
#
#     #semester
#     no_schools = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-map-view/div/div[4]/div[2]/span"
#     no_students = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-map-view/div/div[4]/div[1]/span"
#     zoom_in = "//a[@title='Zoom in']"
#     zoom_out = "//a[@title='Zoom out']"
#     dash_name = "//h4"
#     # list of names
#     SR_Dnames = "//*[@id='choose_dist']/option"
#     SR_Bnames = "//*[@id='choose_block']/option"
#     SR_cnames = "//*[@id='choose_cluster']/option"
#
#
#     crcdist ="/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-map-view/div/div[2]/div[2]/select[1]/option"
#
#     year = "//select[@id='year']/option[1]"
#     monthnames = "//select[@id='month']/option"
#     august = "//select[@id='month']/option[2]"
#     Sept = "//select[@id='month']/option[3]"
#     Oct = "//select[@id='month']/option[4]"
#     blockslist = "//select[@name='myBlock']/option"
#     clusterlist = "//select[@name='myCluster']/option"
#     back = "//a"
#     reg_user = "//a"
#     details = "//div[@class='col-sm-4']/span"
#     # Dash board
#     TAR = "tar"
#     SR = "sr"
#     CRC ="crcr"
#
#     # xpath of Dashboard
#
#     crcvisits = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-bar-chart/div/div[5]/div[1]/span"
#     totalschools = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-bar-chart/div/div[5]/div[2]/span"
#
#     visited = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-bar-chart/div/div[5]/div[3]/span"
#     notvisited = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-bar-chart/div/div[5]/div[4]/span"
#
#     range = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-bar-chart/div/div[5]/div[5]/span"
#
#     # Table in CRC
#     crc_districtwise_csv = "//*[@id='select']/select/option[2]"
#     crc_clusterwise_csv = "//*[@id='select']/select/option[4]"
#     # rowby data
#     distrows = "//tr[@class='odd']/td"
#     headers = "//tr[@role='row']/th"
#     footer = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-crc-report/div[1]/div[5]/div/span"
#
#     crc_districtlist ="//*[@id='dist']/option"
#     crc_blocklist = "//*[@id='block']/option"
#     crc_clusterlist ="//*[@id='cluster']/option"
#
#
#     # select_type
#     distwise = "//select[@name='downloadType']/option[2]"
#     blkwise = "//select[@name='downloadType']/option[3]"
#     clusterwise = "//select[@name='downloadType']/option[4]"
#     schoolwise = "//select[@name='downloadType']/option[5]"
#     # X axis and Y axis
#     xaxis = "//select[@name='xAxis']/option"
#     yaxis = "//select[@name='yAxis']/option"
#
#     crcdistrict = "//select[@name='myDistrict']/option"
#     selecttype = "//*[@id='select']/select/option"
#
#     Notemsg = "//div[@class='col-sm-12']/p/b"
#     value2 = "Anand"
#     # semester Report
#     srDist = "//select[@class='ng-untouched ng-pristine ng-valid']/option"
#     srcluster = "//select[@class='ng-pristine ng-valid ng-touched']/option"
#     srblock = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[2]/option"
#     sr_students = "students"
#     sr_schools ="schools"
#
#     # SR
#
#     SRD1 = "//*[@id='choose_dist']/option[2]"
#     SRD2 = "//*[@id='choose_dist']/option[3]"
#     SRD3 = "//*[@id='choose_dist']/option[4]"
#     SRD4 = "//*[@id='choose_dist']/option[5]"
#     SRD5 = "//*[@id='choose_dist']/option[6]"
#     SRD6 = "//*[@id='choose_dist']/option[7]"
#     SRD7 = "//*[@id='choose_dist']/option[8]"
#     SRD8 = "//*[@id='choose_dist']/option[9]"
#     SRD9 = "//*[@id='choose_dist']/option[10]"
#     SRD10 = "//*[@id='choose_dist']/option[11]"
#     SRD11 = "//*[@id='choose_dist']/option[12]"
#     SRD12 = "//*[@id='choose_dist']/option[13]"
#     SRD13 = "//*[@id='choose_dist']/option[14]"
#     SRD14 = "//*[@id='choose_dist']/option[15]"
#     SRD15 = "//*[@id='choose_dist']/option[16]"
#     SRD16 = "//*[@id='choose_dist']/option[17]"
#     SRD17 = "//*[@id='choose_dist']/option[18]"
#     SRD18 = "//*[@id='choose_dist']/option[19]"
#     SRD19 = "//*[@id='choose_dist']/option[20]"
#     SRD20 = "//*[@id='choose_dist']/option[21]"
#     SRD21 = "//*[@id='choose_dist']/option[22]"
#     SRD22 = "//*[@id='choose_dist']/option[23]"
#     SRD23 = "//*[@id='choose_dist']/option[24]"
#     SRD24 = "//*[@id='choose_dist']/option[25]"
#     SRD25 = "//*[@id='choose_dist']/option[26]"
#     SRD26 = "//*[@id='choose_dist']/option[27]"
#     SRD27 = "//*[@id='choose_dist']/option[28]"
#     SRD28 = "//*[@id='choose_dist']/option[29]"
#     SRD29 = "//*[@id='choose_dist']/option[30]"
#     SRD30 = "//*[@id='choose_dist']/option[31]"
#     SRD31 = "//*[@id='choose_dist']/option[32]"
#     SRD32 = "//*[@id='choose_dist']/option[33]"
#     SRD33 = "//*[@id='choose_dist']/option[34]"
#
#     SRB1 = "//*[@id='choose_block']/option[2]"
#     SRB2 = "//*[@id='choose_block']/option[3]"
#     SRB3 = "//*[@id='choose_block']/option[4]"
#     SRB4 = "//*[@id='choose_block']/option[5]"
#     SRB5 = "//*[@id='choose_block']/option[6]"
#     SRB6 = "//*[@id='choose_block']/option[7]"
#     SRB7 = "//*[@id='choose_block']/option[8]"
#     SRB8 = "//*[@id='choose_block']/option[9]"
#     SRB9 = "//*[@id='choose_block']/option[10]"
#     SRB10 = "//*[@id='choose_block']/option[11]"
#     SRB11 = "//*[@id='choose_block']/option[12]"
#     SRB12 = "//*[@id='choose_block']/option[13]"
#     SRB13 = "//*[@id='choose_block']/option[14]"
#     SRB14 = "//*[@id='choose_block']/option[15]"
#     SRB15 = "//*[@id='choose_block']/option[16]"
#
#     SRC1 = "//*[@id='choose_cluster']/option[2]"
#     SRC2 = "//*[@id='choose_cluster']/option[3]"
#     SRC3 = "//*[@id='choose_cluster']/option[4]"
#     SRC4 = "//*[@id='choose_cluster']/option[5]"
#     SRC5 = "//*[@id='choose_cluster']/option[6]"
#     SRC6 = "//*[@id='choose_cluster']/option[7]"
#     SRC7 = "//*[@id='choose_cluster']/option[8]"
#     SRC8 = "//*[@id='choose_cluster']/option[9]"
#     SRC9 = "//*[@id='choose_cluster']/option[10]"
#     SRC10 = "//*[@id='choose_cluster']/option[11]"
#     SRC11 = "//*[@id='choose_cluster']/option[12]"
#     SRC12 = "//*[@id='choose_cluster']/option[13]"
#     SRC13 = "//*[@id='choose_cluster']/option[14]"
#     SRC14 = "//*[@id='choose_cluster']/option[15]"
#     SRC15 = "//*[@id='choose_cluster']/option[16]"
#     SRC16 = "//*[@id='choose_cluster']/option[17]"
#     SRC17 = "//*[@id='choose_cluster']/option[18]"
#     SRC18 = "//*[@id='choose_cluster']/option[19]"
#     SRC19 = "//*[@id='choose_cluster']/option[20]"
#     SRC20 = "//*[@id='choose_cluster']/option[21]"
#     SRC21 = "//*[@id='choose_cluster']/option[22]"
#     SRC22 = "//*[@id='choose_cluster']/option[23]"
#     SRC23 = "//*[@id='choose_cluster']/option[24]"
#     SRC24 = "//*[@id='choose_cluster']/option[25]"
#     SRC25 = "//*[@id='choose_cluster']/option[26]"
#
#     # SAR
#
#     SARD1 = "//*[@id='choose_dist']/option[2]"
#     SARD2 = "//*[@id='choose_dist']/option[3]"
#     SARD3 = "//*[@id='choose_dist']/option[4]"
#     SARD4 = "//*[@id='choose_dist']/option[5]"
#     SARD5 = "//*[@id='choose_dist']/option[6]"
#     SARD6 = "//*[@id='choose_dist']/option[7]"
#     SARD7 = "//*[@id='choose_dist']/option[8]"
#     SARD8 = "//*[@id='choose_dist']/option[9]"
#     SARD9 = "//*[@id='choose_dist']/option[10]"
#     SARD10 = "//*[@id='choose_dist']/option[11]"
#     SARD11 = "//*[@id='choose_dist']/option[12]"
#     SARD12 = "//*[@id='choose_dist']/option[13]"
#     SARD13 = "//*[@id='choose_dist']/option[14]"
#     SARD14 = "//*[@id='choose_dist']/option[15]"
#     SARD15 = "//*[@id='choose_dist']/option[16]"
#     SARD16 = "//*[@id='choose_dist']/option[17]"
#     SARD17 = "//*[@id='choose_dist']/option[18]"
#     SARD18 = "//*[@id='choose_dist']/option[19]"
#     SARD19 = "//*[@id='choose_dist']/option[20]"
#     SARD20 = "//*[@id='choose_dist']/option[21]"
#     SARD21 = "//*[@id='choose_dist']/option[22]"
#     SARD22 = "//*[@id='choose_dist']/option[23]"
#     SARD23 = "//*[@id='choose_dist']/option[24]"
#     SARD24 = "//*[@id='choose_dist']/option[25]"
#     SARD25 = "//*[@id='choose_dist']/option[26]"
#     SARD26 = "//*[@id='choose_dist']/option[27]"
#     SARD27 = "//*[@id='choose_dist']/option[28]"
#     SARD28 = "//*[@id='choose_dist']/option[29]"
#     SARD29 = "//*[@id='choose_dist']/option[30]"
#     SARD30 = "//*[@id='choose_dist']/option[31]"
#     SARD31 = "//*[@id='choose_dist']/option[32]"
#     SARD32 = "//*[@id='choose_dist']/option[33]"
#     SARD33 = "//*[@id='choose_dist']/option[34]"
#
#     SARB1 = "//*[@id='choose_block']/option[2]"
#     SARB2 = "//*[@id='choose_block']/option[3]"
#     SARB3 = "//*[@id='choose_block']/option[4]"
#     SARB4 = "//*[@id='choose_block']/option[5]"
#     SARB5 = "//*[@id='choose_block']/option[6]"
#     SARB6 = "//*[@id='choose_block']/option[7]"
#     SARB7 = "//*[@id='choose_block']/option[8]"
#     SARB8 = "//*[@id='choose_block']/option[9]"
#     SARB9 = "//*[@id='choose_block']/option[10]"
#     SARB10 = "//*[@id='choose_block']/option[11]"
#     SARB11 = "//*[@id='choose_block']/option[12]"
#     SARB12 = "//*[@id='choose_block']/option[13]"
#     SARB13 = "//*[@id='choose_block']/option[14]"
#     SARB14 = "//*[@id='choose_block']/option[15]"
#     SARB15 = "//*[@id='choose_block']/option[16]"
#
#     SARC1 = "//*[@id='choose_cluster']/option[2]"
#     SARC2 = "//*[@id='choose_cluster']/option[3]"
#     SARC3 = "//*[@id='choose_cluster']/option[4]"
#     SARC4 = "//*[@id='choose_cluster']/option[5]"
#     SARC5 = "//*[@id='choose_cluster']/option[6]"
#     SARC6 = "//*[@id='choose_cluster']/option[7]"
#     SARC7 = "//*[@id='choose_cluster']/option[8]"
#     SARC8 = "//*[@id='choose_cluster']/option[9]"
#     SARC9 = "//*[@id='choose_cluster']/option[10]"
#     SARC10 = "//*[@id='choose_cluster']/option[11]"
#     SARC11 = "//*[@id='choose_cluster']/option[12]"
#     SARC12 = "//*[@id='choose_cluster']/option[13]"
#     SARC13 = "//*[@id='choose_cluster']/option[14]"
#     SARC14 = "//*[@id='choose_cluster']/option[15]"
#     SARC15 = "//*[@id='choose_cluster']/option[16]"
#     SARC16 = "//*[@id='choose_cluster']/option[17]"
#     SARC17 = "//*[@id='choose_cluster']/option[18]"
#     SARC18 = "//*[@id='choose_cluster']/option[19]"
#     SARC19 = "//*[@id='choose_cluster']/option[20]"
#     SARC20 = "//*[@id='choose_cluster']/option[21]"
#     SARC21 = "//*[@id='choose_cluster']/option[22]"
#     SARC22 = "//*[@id='choose_cluster']/option[23]"
#     SARC23 = "//*[@id='choose_cluster']/option[24]"
#     SARC24 = "//*[@id='choose_cluster']/option[25]"
#     SARC25 = "//*[@id='choose_cluster']/option[26]"
#
#
#     # CRC
#
#     CRD1 = "//*[@id='dist']/option[2]"
#     CRD2 = "//*[@id='dist']/option[3]"
#     CRD3 = "//*[@id='dist']/option[4]"
#     CRD4 = "//*[@id='dist']/option[5]"
#     CRD5 = "//*[@id='dist']/option[6]"
#     CRD6 = "//*[@id='dist']/option[7]"
#     CRD7 = "//*[@id='dist']/option[8]"
#     CRD8 = "//*[@id='dist']/option[9]"
#     CRD9 = "//*[@id='dist']/option[10]"
#     CRD10 = "//*[@id='dist']/option[11]"
#     CRD11 = "//*[@id='dist']/option[12]"
#     CRD12 = "//*[@id='dist']/option[13]"
#     CRD13 = "//*[@id='dist']/option[14]"
#     CRD14 = "//*[@id='dist']/option[15]"
#     CRD15 = "//*[@id='dist']/option[16]"
#     CRD16 = "//*[@id='dist']/option[17]"
#     CRD17 = "//*[@id='dist']/option[18]"
#     CRD18 = "//*[@id='dist']/option[19]"
#     CRD19 = "//*[@id='dist']/option[20]"
#     CRD20 = "//*[@id='dist']/option[21]"
#     CRD21 = "//*[@id='dist']/option[22]"
#     CRD22 = "//*[@id='dist']/option[23]"
#     CRD23 = "//*[@id='dist']/option[24]"
#     CRD24 = "//*[@id='dist']/option[25]"
#     CRD25 = "//*[@id='dist']/option[26]"
#     CRD26 = "//*[@id='dist']/option[27]"
#     CRD27 = "//*[@id='dist']/option[28]"
#     CRD28 = "//*[@id='dist']/option[29]"
#     CRD29 = "//*[@id='dist']/option[30]"
#     CRD30 = "//*[@id='dist']/option[31]"
#     CRD31 = "//*[@id='dist']/option[32]"
#     CRD32 = "//*[@id='dist']/option[33]"
#     CRD33 = "//*[@id='dist']/option[34]"
#
#     CRB1 = "//*[@id='block']/option[2]"
#     CRB2 = "//*[@id='block']/option[3]"
#     CRB3 = "//*[@id='block']/option[4]"
#     CRB4 = "//*[@id='block']/option[5]"
#     CRB5 = "//*[@id='block']/option[6]"
#     CRB6 = "//*[@id='block']/option[7]"
#     CRB7 = "//*[@id='block']/option[8]"
#     CRB8 = "//*[@id='block']/option[9]"
#     CRB9 = "//*[@id='block']/option[10]"
#     CRB10 = "//*[@id='block']/option[11]"
#     CRB11 = "//*[@id='block']/option[12]"
#     CRB12 = "//*[@id='block']/option[13]"
#     CRB13 = "//*[@id='block']/option[14]"
#     CRB14 = "//*[@id='block']/option[15]"
#     CRB15 = "//*[@id='block']/option[16]"
#
#     CRC1 = "//*[@id='cluster']/option[2]"
#     CRC2 = "//*[@id='cluster']/option[3]"
#     CRC3 = "//*[@id='cluster']/option[4]"
#     CRC4 = "//*[@id='cluster']/option[5]"
#     CRC5 = "//*[@id='cluster']/option[6]"
#     CRC6 = "//*[@id='cluster']/option[7]"
#     CRC7 = "//*[@id='cluster']/option[8]"
#     CRC8 = "//*[@id='cluster']/option[9]"
#     CRC9 = "//*[@id='cluster']/option[10]"
#     CRC10 = "//*[@id='cluster']/option[11]"
#     CRC11 = "//*[@id='cluster']/option[12]"
#     CRC12 = "//*[@id='cluster']/option[13]"
#     CRC13 = "//*[@id='cluster']/option[14]"
#     CRC14 = "//*[@id='cluster']/option[15]"
#     CRC15 = "//*[@id='cluster']/option[16]"
#     CRC16 = "//*[@id='cluster']/option[17]"
#     CRC17 = "//*[@id='cluster']/option[18]"
#     CRC18 = "//*[@id='cluster']/option[19]"
#     CRC19 = "//*[@id='cluster']/option[20]"
#     CRC20 = "//*[@id='cluster']/option[21]"
#     CRC21 = "//*[@id='cluster']/option[22]"
#     CRC22 = "//*[@id='cluster']/option[23]"
#     CRC23 = "//*[@id='cluster']/option[24]"
#     CRC24 = "//*[@id='cluster']/option[25]"
#     CRC25 = "//*[@id='cluster']/option[26]"
#
#
#

import base64


class Data():
    #path should be chrome.exe file location
    #Path =executable_path="/home/chetan/PycharmProjects/cQube/Driverfile/chromedriver"
    Path =executable_path="/home/devraj/PycharmProjects/SemesterReport/Driver/geckodriver"

    #URL = base64.b64decode("aHR0cHM6Ly9jcXViZS50aWJpbHByb2plY3RzLmNvbQ==").decode("utf-8")
    # username = base64.b64decode("dGliaWxzb2x1dGlvbnNAY3F1YmUuY29t").decode("utf-8")
    # password= base64.b64decode("dGliaWwxMjM=").decode("utf-8")
    # username = "admin@cqube.com"
    # password = "admin123"
    username = "radhika@cqube.com"
    password = "tibil123"
    #URL='http://52.66.209.6:4200/#/login'
    URL = 'https://cqube.tibilprojects.com/#/login'
    email = "//input[@id='exampleInputEmail']"
    pwd = "//input[@id='exampleInputPassword']"
    loginbtn = "//button[@type='submit']"



    zoom_in = "//a[@title='Zoom in']"
    zoom_out = "//a[@title='Zoom out']"

    Blocks ="//button[@class='btn btn-secondary']/b[contains(text(),'Blocks')]"
    Clusters ="//button[@class='btn btn-secondary']/b[contains(text(),'Clusters')]"
    Schools  = "//button[@class='btn btn-secondary']/b[contains(text(),'Schools')]"

    District ="//select[@name='myDistrict']"

    Distoptions = "//select[@name='myDistrict']/option"
    dots = "leaflet-interactive"

    reg_user = "//a"
    back = "//a"


    details="//div[@class='col-sm-4']/span"
    dist1 = "//select[@name='myDistrict']/option[1]"
    blk1 = "//select[@name='myBlock']/option[1]"
    clu1 = "//select[@name='myCluster']/option[1]"

    dist2 ="//select[@name='myDistrict']/option[2]"
    blk2 ="//select[@name='myBlock']/option[2]"
    clu2 = "//select[@name='myCluster']/option[2]"

    dist3="//select[@name='myDistrict']/option[2]"
    blk3 ="//select[@name='myBlock']/option[2]"
    clu3="//select[@name='myCluster']/option[2]"

    dist4 = "//select[@name='myDistrict']/option[4]"
    blk4 = "//select[@name='myBlock']/option[4]"
    clu4 = "//select[@name='myCluster']/option[4]"

    dist5 = "//select[@name='myDistrict']/option[5]"
    blk5 = "//select[@name='myBlock']/option[5]"
    clu5 = "//select[@name='myCluster']/option[5]"

    dist6 = "//select[@name='myDistrict']/option[6]"
    blk6 = "//select[@name='myBlock']/option[6]"
    clu6 = "//select[@name='myCluster']/option[6]"

    dist7 = "//select[@name='myDistrict']/option[7]"
    blk7 = "//select[@name='myBlock']/option[7]"
    clu7 = "//select[@name='myCluster']/option[7]"

    dist8 = "//select[@name='myDistrict']/option[8]"
    dist9 = "//select[@name='myDistrict']/option[9]"
    dist10 = "//select[@name='myDistrict']/option[10]"
    dist11 = "//select[@name='myDistrict']/option[11]"
    dist12= "//select[@name='myDistrict']/option[12]"
    dist13 = "//select[@name='myDistrict']/option[13]"
    dist14 = "//select[@name='myDistrict']/option[14]"
    dist15 = "//select[@name='myDistrict']/option[15]"
    dist16 = "//select[@name='myDistrict']/option[16]"
    dist17 = "//select[@name='myDistrict']/option[17]"
    dist18 = "//select[@name='myDistrict']/option[18]"
    dist19 = "//select[@name='myDistrict']/option[19]"
    dist20 = "//select[@name='myDistrict']/option[20]"

    hyper_link = "//p/span"
    directory ="//p[contains(text(),' Semester report for:')]/span"
    Download ="//img[@title='Download Report']"
# Dash board
    Dashboard ="//span[@class='" \
               "mat-button-wrapper']/mat-icon"
    login_in = "//span[@class='span']"
    SAR = "//div[@class='mat-list-item-content']/td[contains(text(),'Student')]"
    TAR ="//div[@class='mat-list-item-content']/td[contains(text(),'Teacher')]"
    SR  = "//div[@class='mat-list-item-content']/td[contains(text(),'Semester')]"
    crc ="//div[@class='mat-list-item-content']/td[contains(text(),'CRC Reports')]"
    Log_out ="//button/span[contains(text(),'Log Out')]"
    Home_icon ="//img[@id='home']"
    SI = 'si'

    No_schools='/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-student-attendance/div[1]/div[4]/div[2]'
    # select_district = "/html/body/app-root/app-map-view/div/div[2]/div[2]/select[1]"
    # select_blocks = "/html/body/app-root/app-map-view/div/div[2]/div[2]/select[2]"
    # select_clusters = "/html/body/app-root/app-map-view/div/div[2]/div[2]/select[3]"
    select_district='myDistrict'
    select_blocks='myBlock'
    select_clusters='myCluster'
    select_month='month'

    School_infra = "//*[@id='usr']/span/span[contains(text(),'School Infrastructure')]"
    Reportmap = "//*[@id='crtUsr']/div/span[contains(text(),'Report(Map)')]"
    Report = " //*[@id='chPass']/div/span[contains(text(),'Report')]"
    scm_block = "block"
    scm_cluster = "cluster"
    scm_school = "school"
    sc_choosedist = "//select[@id='choose_dist']/option"
    sc_chooseblock = "//select[@id='choose_block']/option"
    sc_choosecluster = "//select[@id='choose_cluster']/option"
    sc_infrascores = "//select[@id='choose_infra']/option"
    sc_no_of_schools = "schools"

    scm_district = "//select[@id='choose_dist']/option[2]"
    scm_blk = "//select[@id='choose_block']/option[2]"
    scm_clust = "//select[@id='choose_cluster']/option[2]"















