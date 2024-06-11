import os
import smtplib
from random import randint
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from src.main.objects.server.Static import getConfigInfo


class MailSender:
    def __init__(self, email_to):
        self.__message = MIMEMultipart(_subtype='related')
        self.__user_email = email_to
        self.__personal_code = int()
        
        self.__server_address = getConfigInfo('email_server', 'address')
        self.__password = getConfigInfo('email_server', 'password')
        self.__host =  getConfigInfo('email_server', 'host')
        self.__port = getConfigInfo('email_server', 'port')

    def sendVerificationEmail(self):
        self.__createMessage(html_text=self.__getVerificationHtmlTemplate())
        server = smtplib.SMTP(self.__host, self.__port)
        with server as smtp:
            smtp.login(self.__server_address, self.__password)
            smtp.send_message(self.__message)
        return self.__personal_code
    
    def sendReportEmail(self, report_by: dict, report_to: dict):
        self.__createMessage(html_text=self.__getReportHtmlTemplate(user_id_1=str(report_by["user_id"]),
                                                                    username_1=str(report_by["username"]),
                                                                    user_id_2=str(report_to["user_id"]),
                                                                    username_2=str(report_to["username"]),
                                                                    post_id=str(report_to["post_id"])))
        server = smtplib.SMTP(self.__host, self.__port)
        with server as smtp:
            smtp.login(self.__server_address, self.__password)
            smtp.send_message(self.__message)
        return None
    
    def __createMessage(self, html_text):
        self.__message['From'] = self.__server_address
        self.__message['To'] = self.__user_email

        text = MIMEText(html_text, 'html')
        self.__message.attach(text)

        image_path = os.path.dirname(os.path.abspath(__file__))[:-14] + "gui/resources/images/PngLogo.png"
        img_data = open(image_path, 'rb').read()
        img = MIMEImage(img_data, 'png')
        img.add_header('Content-Id', '<image1>')
        self.__message.attach(img)

        return None
    
    def __getVerificationHtmlTemplate(self):
        self.__message['Subject'] = "R&R: Access confirmation"
        self.__personal_code = randint(100000, 999999)
        return """
<!DOCTYPE html>
<html xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en">

<head>
    <title></title>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="x-apple-disable-message-reformatting" content="">
    <meta content="target-densitydpi=device-dpi" name="viewport">
    <meta content="true" name="HandheldFriendly">
    <meta content="width=device-width" name="viewport">
    <meta name="format-detection" content="telephone=no, date=no, address=no, email=no, url=no">
    <style type="text/css">
        table {
            border-collapse: separate;
            table-layout: fixed;
            mso-table-lspace: 0pt;
            mso-table-rspace: 0pt
        }

        table td {
            border-collapse: collapse
        }

        .ExternalClass {
            width: 100%
        }

        .ExternalClass,
        .ExternalClass p,
        .ExternalClass span,
        .ExternalClass font,
        .ExternalClass td,
        .ExternalClass div {
            line-height: 100%
        }

        body,
        a,
        li,
        p,
        h1,
        h2,
        h3 {
            -ms-text-size-adjust: 100%;
            -webkit-text-size-adjust: 100%;
        }

        html {
            -webkit-text-size-adjust: none !important
        }

        body,
        #innerTable {
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale
        }

        #innerTable img+div {
            display: none;
            display: none !important
        }

        img {
            Margin: 0;
            padding: 0;
            -ms-interpolation-mode: bicubic
        }

        h1,
        h2,
        h3,
        p,
        a {
            line-height: inherit;
            overflow-wrap: normal;
            white-space: normal;
            word-break: break-word
        }

        a {
            text-decoration: none
        }

        h1,
        h2,
        h3,
        p {
            min-width: 100% !important;
            width: 100% !important;
            max-width: 100% !important;
            display: inline-block !important;
            border: 0;
            padding: 0;
            margin: 0
        }

        a[x-apple-data-detectors] {
            color: inherit !important;
            text-decoration: none !important;
            font-size: inherit !important;
            font-family: inherit !important;
            font-weight: inherit !important;
            line-height: inherit !important
        }

        u+#body a {
            color: inherit;
            text-decoration: none;
            font-size: inherit;
            font-family: inherit;
            font-weight: inherit;
            line-height: inherit;
        }

        a[href^="mailto"],
        a[href^="tel"],
        a[href^="sms"] {
            color: inherit;
            text-decoration: none
        }

        img,
        p {
            margin: 0;
            Margin: 0;
            font-family: Lato, BlinkMacSystemFont, Segoe UI, Helvetica Neue, Arial, sans-serif;
            line-height: 22px;
            font-weight: 400;
            font-style: normal;
            font-size: 16px;
            text-decoration: none;
            text-transform: none;
            letter-spacing: 0;
            direction: ltr;
            color: #333;
            text-align: left;
            mso-line-height-rule: exactly;
            mso-text-raise: 2px
        }

        h1 {
            margin: 0;
            Margin: 0;
            font-family: Roboto, BlinkMacSystemFont, Segoe UI, Helvetica Neue, Arial, sans-serif;
            line-height: 34px;
            font-weight: 400;
            font-style: normal;
            font-size: 28px;
            text-decoration: none;
            text-transform: none;
            letter-spacing: 0;
            direction: ltr;
            color: #333;
            text-align: left;
            mso-line-height-rule: exactly;
            mso-text-raise: 2px
        }

        h2 {
            margin: 0;
            Margin: 0;
            font-family: Lato, BlinkMacSystemFont, Segoe UI, Helvetica Neue, Arial, sans-serif;
            line-height: 30px;
            font-weight: 400;
            font-style: normal;
            font-size: 24px;
            text-decoration: none;
            text-transform: none;
            letter-spacing: 0;
            direction: ltr;
            color: #333;
            text-align: left;
            mso-line-height-rule: exactly;
            mso-text-raise: 2px
        }

        h3 {
            margin: 0;
            Margin: 0;
            font-family: Lato, BlinkMacSystemFont, Segoe UI, Helvetica Neue, Arial, sans-serif;
            line-height: 26px;
            font-weight: 400;
            font-style: normal;
            font-size: 20px;
            text-decoration: none;
            text-transform: none;
            letter-spacing: 0;
            direction: ltr;
            color: #333;
            text-align: left;
            mso-line-height-rule: exactly;
            mso-text-raise: 2px
        }
    </style>
    <style type="text/css">
        @media (min-width: 481px) {
            .hd {
                display: none !important
            }
        }
    </style>
    <style type="text/css">
        @media (max-width: 480px) {
            .hm {
                display: none !important
            }
        }
    </style>
    <style type="text/css">
        @media (min-width: 481px) {

            h1,
            img,
            p {
                margin: 0;
                Margin: 0
            }

            img,
            p {
                font-family: Lato, BlinkMacSystemFont, Segoe UI, Helvetica Neue, Arial, sans-serif;
                line-height: 22px;
                font-weight: 400;
                font-style: normal;
                font-size: 16px;
                text-decoration: none;
                text-transform: none;
                letter-spacing: 0;
                direction: ltr;
                color: #333;
                text-align: left;
                mso-line-height-rule: exactly;
                mso-text-raise: 2px
            }

            h1 {
                font-family: Roboto, BlinkMacSystemFont, Segoe UI, Helvetica Neue, Arial, sans-serif;
                line-height: 34px;
                font-weight: 400;
                font-style: normal;
                font-size: 28px;
                text-decoration: none;
                text-transform: none;
                letter-spacing: 0;
                direction: ltr;
                color: #333;
                text-align: left;
                mso-line-height-rule: exactly;
                mso-text-raise: 2px
            }

            h2,
            h3 {
                margin: 0;
                Margin: 0;
                font-family: Lato, BlinkMacSystemFont, Segoe UI, Helvetica Neue, Arial, sans-serif;
                font-weight: 400;
                font-style: normal;
                text-decoration: none;
                text-transform: none;
                letter-spacing: 0;
                direction: ltr;
                color: #333;
                text-align: left;
                mso-line-height-rule: exactly;
                mso-text-raise: 2px
            }

            h2 {
                line-height: 30px;
                font-size: 24px
            }

            h3 {
                line-height: 26px;
                font-size: 20px
            }

            .t27,
            .t30 {
                width: 600px !important
            }

            .t6 {
                width: 589px !important
            }

            .t17 {
                width: 560px !important
            }
        }
    </style>
    <style type="text/css" media="screen and (min-width:481px)">
        .moz-text-html img,
        .moz-text-html p {
            margin: 0;
            Margin: 0;
            font-family: Lato, BlinkMacSystemFont, Segoe UI, Helvetica Neue, Arial, sans-serif;
            line-height: 22px;
            font-weight: 400;
            font-style: normal;
            font-size: 16px;
            text-decoration: none;
            text-transform: none;
            letter-spacing: 0;
            direction: ltr;
            color: #333;
            text-align: left;
            mso-line-height-rule: exactly;
            mso-text-raise: 2px
        }

        .moz-text-html h1 {
            margin: 0;
            Margin: 0;
            font-family: Roboto, BlinkMacSystemFont, Segoe UI, Helvetica Neue, Arial, sans-serif;
            line-height: 34px;
            font-weight: 400;
            font-style: normal;
            font-size: 28px;
            text-decoration: none;
            text-transform: none;
            letter-spacing: 0;
            direction: ltr;
            color: #333;
            text-align: left;
            mso-line-height-rule: exactly;
            mso-text-raise: 2px
        }

        .moz-text-html h2 {
            margin: 0;
            Margin: 0;
            font-family: Lato, BlinkMacSystemFont, Segoe UI, Helvetica Neue, Arial, sans-serif;
            line-height: 30px;
            font-weight: 400;
            font-style: normal;
            font-size: 24px;
            text-decoration: none;
            text-transform: none;
            letter-spacing: 0;
            direction: ltr;
            color: #333;
            text-align: left;
            mso-line-height-rule: exactly;
            mso-text-raise: 2px
        }

        .moz-text-html h3 {
            margin: 0;
            Margin: 0;
            font-family: Lato, BlinkMacSystemFont, Segoe UI, Helvetica Neue, Arial, sans-serif;
            line-height: 26px;
            font-weight: 400;
            font-style: normal;
            font-size: 20px;
            text-decoration: none;
            text-transform: none;
            letter-spacing: 0;
            direction: ltr;
            color: #333;
            text-align: left;
            mso-line-height-rule: exactly;
            mso-text-raise: 2px
        }

        .moz-text-html .t27,
        .moz-text-html .t30 {
            width: 600px !important
        }

        .moz-text-html .t6 {
            width: 589px !important
        }

        .moz-text-html .t17 {
            width: 560px !important
        }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Fira+Sans:wght@400;500&amp;display=swap" rel="stylesheet"
        type="text/css">
</head>

<body id="body" class="t34" style="min-width:100%;Margin:0px;padding:0px;background-color:#F0F0F0;">
    <div class="t33" style="background-color:#F0F0F0;">
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" align="center">
            <tr>
                <td class="t32" style="font-size:0;line-height:0;mso-line-height-rule:exactly;background-color:#F0F0F0;"
                    valign="top" align="center">
                    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" align="center"
                        id="innerTable">
                        <tr>
                            <td>
                                <table class="t28" role="presentation" cellpadding="0" cellspacing="0"
                                    style="Margin-left:auto;Margin-right:auto;">
                                    <tr>
                                        <td class="t27" style="background-color:#FFFFFF;width:480px;">
                                            <div class="t26"
                                                style="display:inline-table;width:100%;text-align:center;vertical-align:top;">
                                                <div class="t25"
                                                    style="display:inline-table;text-align:initial;vertical-align:inherit;width:100%;max-width:600px;">
                                                    <table role="presentation" width="100%" cellpadding="0"
                                                        cellspacing="0" class="t24">
                                                        <tr>
                                                            <td class="t23" style="background-color:#F8F2F0;">
                                                                <table role="presentation" width="100%" cellpadding="0"
                                                                    cellspacing="0">
                                                                    <tr>
                                                                        <td>
                                                                            <div class="t1"
                                                                                style="mso-line-height-rule:exactly;mso-line-height-alt:125px;line-height:125px;font-size:1px;display:block;">
                                                                                &nbsp;&nbsp;
                                                                            </div>
                                                                        </td>
                                                                    </tr>
                                                                    <tr>
                                                                        <td>
                                                                            <table class="t3" role="presentation"
                                                                                cellpadding="0" cellspacing="0"
                                                                                style="Margin-left:auto;Margin-right:auto;">
                                                                                <tr>
                                                                                    <td class="t2" style="width:144px;">
                                                                                        <div style="font-size:0px;"><img
                                                                                                class="t0"
                                                                                                style="display:block;border:0;height:auto;width:100%;Margin:0;max-width:100%;"
                                                                                                width="144"
                                                                                                height="53.890625"
                                                                                                alt="1"
                                                                                                src="cid:image1">
                                                                                        </div>
                                                                                    </td>
                                                                                </tr>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                    <tr>
                                                                        <td>
                                                                            <div class="t5"
                                                                                style="mso-line-height-rule:exactly;mso-line-height-alt:55px;line-height:55px;font-size:1px;display:block;">
                                                                                &nbsp;&nbsp;
                                                                            </div>
                                                                        </td>
                                                                    </tr>
                                                                    <tr>
                                                                        <td>
                                                                            <table class="t7" role="presentation"
                                                                                cellpadding="0" cellspacing="0"
                                                                                style="Margin-left:auto;Margin-right:auto;">
                                                                                <tr>
                                                                                    <td class="t6" style="width:480px;">
                                                                                        <h1 class="t4"
                                                                                            style="margin:0;Margin:0;font-family:Arial,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:52px;font-weight:700;font-style:normal;font-size:48px;text-decoration:none;text-transform:none;direction:ltr;color:#000000;text-align:center;mso-line-height-rule:exactly;mso-text-raise:1px;">
                                                                                            YOUR PERSONAL CODE</h1>
                                                                                    </td>
                                                                                </tr>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                    <tr>
                                                                        <td>
                                                                            <div class="t8"
                                                                                style="mso-line-height-rule:exactly;mso-line-height-alt:30px;line-height:30px;font-size:1px;display:block;">
                                                                                &nbsp;&nbsp;
                                                                            </div>
                                                                        </td>
                                                                    </tr>
                                                                    <tr>
                                                                        <td>
                                                                            <table class="t11" role="presentation"
                                                                                cellpadding="0" cellspacing="0"
                                                                                style="Margin-left:auto;Margin-right:auto;">
                                                                                <tr>
                                                                                    <td class="t10"
                                                                                        style="width:350px;">
                                                                                        <p class="t9"
                                                                                            style="margin:0;Margin:0;font-family:Fira Sans,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:30px;font-weight:500;font-style:normal;font-size:20px;text-decoration:none;text-transform:none;direction:ltr;color:#666666;text-align:center;mso-line-height-rule:exactly;mso-text-raise:3px;">
                                                                                            To make sure it's you, enter
                                                                                            your code in R&amp;R.</p>
                                                                                    </td>
                                                                                </tr>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                    <tr>
                                                                        <td>
                                                                            <table class="t18" role="presentation"
                                                                                cellpadding="0" cellspacing="0"
                                                                                style="Margin-left:auto;Margin-right:auto;">
                                                                                <tr>
                                                                                    <td class="t17"
                                                                                        style="width:440px;padding:20px 20px 20px 20px;">
                                                                                        <table role="presentation"
                                                                                            width="100%" cellpadding="0"
                                                                                            cellspacing="0">
                                                                                            <tr>
                                                                                                <td>
                                                                                                    <div class="t13"
                                                                                                        style="mso-line-height-rule:exactly;mso-line-height-alt:40px;line-height:40px;font-size:1px;display:block;">
                                                                                                        &nbsp;&nbsp;
                                                                                                    </div>
                                                                                                </td>
                                                                                            </tr>
                                                                                            <tr>
                                                                                                <td>
                                                                                                    <table class="t15"
                                                                                                        role="presentation"
                                                                                                        cellpadding="0"
                                                                                                        cellspacing="0"
                                                                                                        style="Margin-left:auto;Margin-right:auto;">
                                                                                                        <tr>
                                                                                                            <td class="t14"
                                                                                                                style="background-color:#DDDDDD;overflow:hidden;width:308px;border-radius:14px 14px 14px 14px;">
                                                                                                                <p class="t12"
                                                                                                                    style="margin:0;Margin:0;font-family:Arial,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:58px;font-weight:700;font-style:normal;font-size:32px;text-decoration:none;text-transform:none;direction:ltr;color:#000000;text-align:center;mso-line-height-rule:exactly;mso-text-raise:8px;">""" + " " + str(self.__personal_code) + "\n" + \
                                                                                                                """</p>
                                                                                                            </td>
                                                                                                        </tr>
                                                                                                    </table>
                                                                                                </td>
                                                                                            </tr>
                                                                                            <tr>
                                                                                                <td>
                                                                                                    <div class="t16"
                                                                                                        style="mso-line-height-rule:exactly;mso-line-height-alt:60px;line-height:60px;font-size:1px;display:block;">
                                                                                                        &nbsp;&nbsp;
                                                                                                    </div>
                                                                                                </td>
                                                                                            </tr>
                                                                                        </table>
                                                                                    </td>
                                                                                </tr>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                    <tr>
                                                                        <td>
                                                                            <table class="t21" role="presentation"
                                                                                cellpadding="0" cellspacing="0"
                                                                                style="Margin-left:auto;Margin-right:auto;">
                                                                                <tr>
                                                                                    <td class="t20"
                                                                                        style="width:350px;">
                                                                                        <p class="t19"
                                                                                            style="margin:0;Margin:0;font-family:Fira Sans,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:25px;font-weight:400;font-style:normal;font-size:16px;text-decoration:none;text-transform:none;direction:ltr;color:#BBBBBB;text-align:center;mso-line-height-rule:exactly;mso-text-raise:3px;">
                                                                                            Do not share your personal
                                                                                            code with anyone. The code
                                                                                            will be valid for 1.5 minutes
                                                                                            from the time of the
                                                                                            request.</p>
                                                                                    </td>
                                                                                </tr>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                    <tr>
                                                                        <td>
                                                                            <div class="t22"
                                                                                style="mso-line-height-rule:exactly;mso-line-height-alt:125px;line-height:125px;font-size:1px;display:block;">
                                                                                &nbsp;&nbsp;
                                                                            </div>
                                                                        </td>
                                                                    </tr>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </div>
                                            </div>
                                        </td>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <table class="t31" role="presentation" cellpadding="0" cellspacing="0"
                                    style="Margin-left:auto;Margin-right:auto;">
                                    <tr>
                                        <td class="t30" style="width:480px;">
                                            <div class="t29"
                                                style="display:inline-table;width:100%;text-align:center;vertical-align:top;">
                                            </div>
                                        </td>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
        </table>
    </div>
</body>

</html>
"""

    def __getReportHtmlTemplate(self, user_id_1: str, username_1: str,
                                      user_id_2: str, username_2: str,
                                      post_id: str):
        self.__message['Subject'] = "R&R: New report"
        return """
<!--
* This email was built using Tabular.
* For more information, visit https://tabular.email
-->
<!DOCTYPE html>
<html lang="en">
<head>
	<title></title>
	<meta charset="UTF-8">
	<meta content="text/html; charset=utf-8" http-equiv="Content-Type"><!--[if !mso]>-->
	<meta content="IE=edge" http-equiv="X-UA-Compatible"><!--<![endif]-->
	<meta content="" name="x-apple-disable-message-reformatting">
	<meta content="target-densitydpi=device-dpi" name="viewport">
	<meta content="true" name="HandheldFriendly">
	<meta content="width=device-width" name="viewport">
	<meta content="telephone=no, date=no, address=no, email=no, url=no" name="format-detection">
	<style type="text/css">
	table {
	border-collapse: separate;
	table-layout: fixed;
	mso-table-lspace: 0pt;
	mso-table-rspace: 0pt
	}
	table td {
	border-collapse: collapse
	}
	.ExternalClass {
	width: 100%
	}
	.ExternalClass,
	.ExternalClass p,
	.ExternalClass span,
	.ExternalClass font,
	.ExternalClass td,
	.ExternalClass div {
	line-height: 100%
	}
	body, a, li, p, h1, h2, h3 {
	-ms-text-size-adjust: 100%;
	-webkit-text-size-adjust: 100%;
	}
	html {
	-webkit-text-size-adjust: none !important
	}
	body, #innerTable {
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale
	}
	#innerTable img+div {
	display: none;
	display: none !important
	}
	img {
	Margin: 0;
	padding: 0;
	-ms-interpolation-mode: bicubic
	}
	h1, h2, h3, p, a {
	line-height: inherit;
	overflow-wrap: normal;
	white-space: normal;
	word-break: break-word
	}
	a {
	text-decoration: none
	}
	h1, h2, h3, p {
	min-width: 100%!important;
	width: 100%!important;
	max-width: 100%!important;
	display: inline-block!important;
	border: 0;
	padding: 0;
	margin: 0
	}
	a[x-apple-data-detectors] {
	color: inherit !important;
	text-decoration: none !important;
	font-size: inherit !important;
	font-family: inherit !important;
	font-weight: inherit !important;
	line-height: inherit !important
	}
	u + #body a {
	color: inherit;
	text-decoration: none;
	font-size: inherit;
	font-family: inherit;
	font-weight: inherit;
	line-height: inherit;
	}
	a[href^="mailto"],
	a[href^="tel"],
	a[href^="sms"] {
	color: inherit;
	text-decoration: none
	}
	img,p{margin:0;Margin:0;font-family:Lato,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:22px;font-weight:400;font-style:normal;font-size:16px;text-decoration:none;text-transform:none;letter-spacing:0;direction:ltr;color:#333;text-align:left;mso-line-height-rule:exactly;mso-text-raise:2px}h1{margin:0;Margin:0;font-family:Roboto,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:34px;font-weight:400;font-style:normal;font-size:28px;text-decoration:none;text-transform:none;letter-spacing:0;direction:ltr;color:#333;text-align:left;mso-line-height-rule:exactly;mso-text-raise:2px}h2{margin:0;Margin:0;font-family:Lato,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:30px;font-weight:400;font-style:normal;font-size:24px;text-decoration:none;text-transform:none;letter-spacing:0;direction:ltr;color:#333;text-align:left;mso-line-height-rule:exactly;mso-text-raise:2px}h3{margin:0;Margin:0;font-family:Lato,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:26px;font-weight:400;font-style:normal;font-size:20px;text-decoration:none;text-transform:none;letter-spacing:0;direction:ltr;color:#333;text-align:left;mso-line-height-rule:exactly;mso-text-raise:2px}
	</style>
	<style type="text/css">
	@media (min-width: 481px) {
	.hd { display: none!important }
	}
	</style>
	<style type="text/css">
	@media (max-width: 480px) {
	.hm { display: none!important }
	}
	</style>
	<style type="text/css">
	@media (min-width: 481px) {
	h1,img,p{margin:0;Margin:0}img,p{font-family:Lato,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:22px;font-weight:400;font-style:normal;font-size:16px;text-decoration:none;text-transform:none;letter-spacing:0;direction:ltr;color:#333;text-align:left;mso-line-height-rule:exactly;mso-text-raise:2px}h1{font-family:Roboto,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:34px;font-weight:400;font-style:normal;font-size:28px;text-decoration:none;text-transform:none;letter-spacing:0;direction:ltr;color:#333;text-align:left;mso-line-height-rule:exactly;mso-text-raise:2px}h2,h3{margin:0;Margin:0;font-family:Lato,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;font-weight:400;font-style:normal;text-decoration:none;text-transform:none;letter-spacing:0;direction:ltr;color:#333;text-align:left;mso-line-height-rule:exactly;mso-text-raise:2px}h2{line-height:30px;font-size:24px}h3{line-height:26px;font-size:20px}.t24,.t27{width:600px!important}.t6{width:589px!important}.t13{width:494px!important}
	}
	</style>
	<style media="screen and (min-width:481px)" type="text/css">
	.moz-text-html img,.moz-text-html p{margin:0;Margin:0;font-family:Lato,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:22px;font-weight:400;font-style:normal;font-size:16px;text-decoration:none;text-transform:none;letter-spacing:0;direction:ltr;color:#333;text-align:left;mso-line-height-rule:exactly;mso-text-raise:2px}.moz-text-html h1{margin:0;Margin:0;font-family:Roboto,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:34px;font-weight:400;font-style:normal;font-size:28px;text-decoration:none;text-transform:none;letter-spacing:0;direction:ltr;color:#333;text-align:left;mso-line-height-rule:exactly;mso-text-raise:2px}.moz-text-html h2{margin:0;Margin:0;font-family:Lato,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:30px;font-weight:400;font-style:normal;font-size:24px;text-decoration:none;text-transform:none;letter-spacing:0;direction:ltr;color:#333;text-align:left;mso-line-height-rule:exactly;mso-text-raise:2px}.moz-text-html h3{margin:0;Margin:0;font-family:Lato,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:26px;font-weight:400;font-style:normal;font-size:20px;text-decoration:none;text-transform:none;letter-spacing:0;direction:ltr;color:#333;text-align:left;mso-line-height-rule:exactly;mso-text-raise:2px}.moz-text-html .t24,.moz-text-html .t27{width:600px!important}.moz-text-html .t6{width:589px!important}.moz-text-html .t13{width:494px!important}
	</style><!--[if !mso]>-->
	<link href="https://fonts.googleapis.com/css2?family=Fira+Sans:wght@400;500&amp;display=swap" rel="stylesheet" type="text/css"><!--<![endif]-->
	<!--[if mso]>
<style type="text/css">
img,p{margin:0;Margin:0;font-family:Lato,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:22px;font-weight:400;font-style:normal;font-size:16px;text-decoration:none;text-transform:none;letter-spacing:0;direction:ltr;color:#333;text-align:left;mso-line-height-rule:exactly;mso-text-raise:2px}h1{margin:0;Margin:0;font-family:Roboto,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:34px;font-weight:400;font-style:normal;font-size:28px;text-decoration:none;text-transform:none;letter-spacing:0;direction:ltr;color:#333;text-align:left;mso-line-height-rule:exactly;mso-text-raise:2px}h2{margin:0;Margin:0;font-family:Lato,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:30px;font-weight:400;font-style:normal;font-size:24px;text-decoration:none;text-transform:none;letter-spacing:0;direction:ltr;color:#333;text-align:left;mso-line-height-rule:exactly;mso-text-raise:2px}h3{margin:0;Margin:0;font-family:Lato,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:26px;font-weight:400;font-style:normal;font-size:20px;text-decoration:none;text-transform:none;letter-spacing:0;direction:ltr;color:#333;text-align:left;mso-line-height-rule:exactly;mso-text-raise:2px}
</style>
<![endif]-->
	<!--[if mso]>
<xml>
<o:OfficeDocumentSettings>
<o:AllowPNG/>
<o:PixelsPerInch>96</o:PixelsPerInch>
</o:OfficeDocumentSettings>
</xml>
<![endif]-->
</head>
<body class="t31" id="body" style="min-width:100%;Margin:0px;padding:0px;background-color:#F0F0F0;">
	<div class="t30" style="background-color:#F0F0F0;">
		<table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%">
			<tr>
				<td align="center" class="t29" style="font-size:0;line-height:0;mso-line-height-rule:exactly;background-color:#F0F0F0;" valign="top">
					<!--[if mso]>
<v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="true" stroke="false">
<v:fill color="#F0F0F0"/>
</v:background>
<![endif]-->
					<table align="center" border="0" cellpadding="0" cellspacing="0" id="innerTable" role="presentation" width="100%">
						<tr>
							<td>
								<!--[if mso]>
<table class="t25" role="presentation" cellpadding="0" cellspacing="0" align="center">
<![endif]-->
								<!--[if !mso]>-->
								<table cellpadding="0" cellspacing="0" class="t25" role="presentation" style="Margin-left:auto;Margin-right:auto;">
									<!--<![endif]-->
									<tr>
										<!--[if mso]>
<td class="t24" style="background-color:#FFFFFF;width:600px;">
<![endif]-->
										<!--[if !mso]>-->
										<td class="t24" style="background-color:#FFFFFF;width:480px;">
											<!--<![endif]-->
											<div class="t23" style="display:inline-table;width:100%;text-align:center;vertical-align:top;">
												<!--[if mso]>
<table role="presentation" cellpadding="0" cellspacing="0" align="center" valign="top" width="600"><tr><td width="600" valign="top"><![endif]-->
												<div class="t22" style="display:inline-table;text-align:initial;vertical-align:inherit;width:100%;max-width:600px;">
													<table cellpadding="0" cellspacing="0" class="t21" role="presentation" width="100%">
														<tr>
															<td class="t20" style="background-color:#F8F2F0;">
																<table cellpadding="0" cellspacing="0" role="presentation" width="100%">
																	<tr>
																		<td>
																			<div class="t1" style="mso-line-height-rule:exactly;mso-line-height-alt:125px;line-height:125px;font-size:1px;display:block;">
																				&nbsp;&nbsp;
																			</div>
																		</td>
																	</tr>
																	<tr>
																		<td>
																			<!--[if mso]>
<table class="t3" role="presentation" cellpadding="0" cellspacing="0" align="center">
<![endif]-->
																			<!--[if !mso]>-->
																			<table cellpadding="0" cellspacing="0" class="t3" role="presentation" style="Margin-left:auto;Margin-right:auto;">
																				<!--<![endif]-->
																				<tr>
																					<!--[if mso]>
<td class="t2" style="width:144px;">
<![endif]-->
																					<!--[if !mso]>-->
																					<td class="t2" style="width:144px;">
																						<!--<![endif]-->
																						<div style="font-size:0px;"><img alt="" class="t0" height="53.890625" src="cid:image1" style="display:block;border:0;height:auto;width:100%;Margin:0;max-width:100%;" width="144"></div>
																					</td>
																				</tr>
																			</table>
																		</td>
																	</tr>
																	<tr>
																		<td>
																			<div class="t5" style="mso-line-height-rule:exactly;mso-line-height-alt:55px;line-height:55px;font-size:1px;display:block;">
																				&nbsp;&nbsp;
																			</div>
																		</td>
																	</tr>
																	<tr>
																		<td>
																			<!--[if mso]>
<table class="t7" role="presentation" cellpadding="0" cellspacing="0" align="center">
<![endif]-->
																			<!--[if !mso]>-->
																			<table cellpadding="0" cellspacing="0" class="t7" role="presentation" style="Margin-left:auto;Margin-right:auto;">
																				<!--<![endif]-->
																				<tr>
																					<!--[if mso]>
<td class="t6" style="width:589px;">
<![endif]-->
																					<!--[if !mso]>-->
																					<td class="t6" style="width:480px;">
																						<!--<![endif]-->
																						<h1 class="t4" style="margin:0;Margin:0;font-family:Arial,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:52px;font-weight:700;font-style:normal;font-size:48px;text-decoration:none;text-transform:none;direction:ltr;color:#000000;text-align:center;mso-line-height-rule:exactly;mso-text-raise:1px;">NEW REPORT</h1>
																					</td>
																				</tr>
																			</table>
																		</td>
																	</tr>
																	<tr>
																		<td>
																			<div class="t8" style="mso-line-height-rule:exactly;mso-line-height-alt:30px;line-height:30px;font-size:1px;display:block;">
																				&nbsp;&nbsp;
																			</div>
																		</td>
																	</tr>
																	<tr>
																		<td>
																			<!--[if mso]>
<table class="t14" role="presentation" cellpadding="0" cellspacing="0" align="center">
<![endif]-->
																			<!--[if !mso]>-->
																			<table cellpadding="0" cellspacing="0" class="t14" role="presentation" style="Margin-left:auto;Margin-right:auto;">
																				<!--<![endif]-->
																				<tr>
																					<!--[if mso]>
<td class="t13" style="width:494px;">
<![endif]-->
																					<!--[if !mso]>-->
																					<td class="t13" style="width:480px;">
																						<!--<![endif]-->
																						<p class="t12" style="margin:0;Margin:0;font-family:Fira Sans,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:30px;font-weight:500;font-style:normal;font-size:20px;text-decoration:none;text-transform:none;direction:ltr;color:#000000;text-align:center;mso-line-height-rule:exactly;mso-text-raise:3px;">User @""" + username_1 + """ (<span class="t9" style="margin:0;Margin:0;font-family:Arial,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;font-weight:700;text-decoration:none;mso-line-height-rule:exactly;background-color:#DDDDDD;">user_id: """ + user_id_1 + """</span>) reported a violation of rules in post (<span class="t10" style="margin:0;Margin:0;mso-line-height-rule:exactly;background-color:#DDDDDD;">post_id: """ + post_id + """</span>) by user @""" + username_2 + """ (<span class="t11" style="margin:0;Margin:0;mso-line-height-rule:exactly;background-color:#DDDDDD;">user_id: """ + user_id_2 + """</span>)</p>
																					</td>
																				</tr>
																			</table>
																		</td>
																	</tr>
																	<tr>
																		<td>
																			<div class="t16" style="mso-line-height-rule:exactly;mso-line-height-alt:45px;line-height:45px;font-size:1px;display:block;">
																				&nbsp;&nbsp;
																			</div>
																		</td>
																	</tr>
																	<tr>
																		<td>
																			<!--[if mso]>
<table class="t18" role="presentation" cellpadding="0" cellspacing="0" align="center">
<![endif]-->
																			<!--[if !mso]>-->
																			<table cellpadding="0" cellspacing="0" class="t18" role="presentation" style="Margin-left:auto;Margin-right:auto;">
																				<!--<![endif]-->
																				<tr>
																					<!--[if mso]>
<td class="t17" style="width:350px;">
<![endif]-->
																					<!--[if !mso]>-->
																					<td class="t17" style="width:350px;">
																						<!--<![endif]-->
																						<p class="t15" style="margin:0;Margin:0;font-family:Fira Sans,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:25px;font-weight:400;font-style:normal;font-size:16px;text-decoration:none;text-transform:none;direction:ltr;color:#000000;text-align:center;mso-line-height-rule:exactly;mso-text-raise:3px;">Dear admin, review the report and take action as soon as possible!</p>
																					</td>
																				</tr>
																			</table>
																		</td>
																	</tr>
																	<tr>
																		<td>
																			<div class="t19" style="mso-line-height-rule:exactly;mso-line-height-alt:125px;line-height:125px;font-size:1px;display:block;">
																				&nbsp;&nbsp;
																			</div>
																		</td>
																	</tr>
																</table>
															</td>
														</tr>
													</table>
												</div><!--[if mso]>
</td>
</tr></table>
<![endif]-->
											</div>
										</td>
									</tr>
								</table>
							</td>
						</tr>
						<tr>
							<td>
								<!--[if mso]>
<table class="t28" role="presentation" cellpadding="0" cellspacing="0" align="center">
<![endif]-->
								<!--[if !mso]>-->
								<table cellpadding="0" cellspacing="0" class="t28" role="presentation" style="Margin-left:auto;Margin-right:auto;">
									<!--<![endif]-->
									<tr>
										<!--[if mso]>
<td class="t27" style="width:600px;">
<![endif]-->
										<!--[if !mso]>-->
										<td class="t27" style="width:480px;">
											<!--<![endif]-->
											<div class="t26" style="display:inline-table;width:100%;text-align:center;vertical-align:top;">
												<!--[if mso]>
<table role="presentation" cellpadding="0" cellspacing="0" align="center" valign="top"><tr>
</tr></table>
<![endif]-->
											</div>
										</td>
									</tr>
								</table>
							</td>
						</tr>
					</table>
				</td>
			</tr>
		</table>
	</div>
</body>
</html>
"""