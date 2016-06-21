# encoding: utf-8
def sendMail(contents="null",sendTo="2553041586@qq.com"):
    import smtplib
    from email.mime.text import MIMEText
    sender = "20154409@stu.neu.edu.cn"
    receivers = ["601495226@qq.com"]
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect("smtp.stu.neu.edu.cn", "25")
        state = smtpObj.login("20154409@stu.neu.edu.cn", "606129")
        msg = MIMEText(contents)
        msg['Subject'] = '爱你没有其他理由'
        msg['From'] = "20154409@stu.neu.edu.cn"
        msg['To'] = "601495226@qq.com"
        if state[0] == 235:
            smtpObj.sendmail(sender, receivers, msg.as_string())
            print "邮件发送成功"
            smtpObj.quit()
    except smtplib.SMTPException, e:
        print str(e)

c = "徐滔我爱你"
sendMail(c)
