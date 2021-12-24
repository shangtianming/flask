import smtplib
from email.mime.text import MIMEText
#下面注释的是公司jenkins登录发送逻辑
#为什么会不同，是因为jenkins配置的原因，参考我之前的文章：https://www.cnblogs.com/yinwenbin/p/10502490.html


class SendMail:
    # def __init__(self, host="mail.testhz.com", user="jenkins", pwd="nW6qQdUz", postfix="testhz.com"):
    def __init__(self, host="smtp.163.com", user="个人邮箱", pwd="个人邮箱的授权码"):
        self.host = host
        self.user = user
        self.pwd = pwd
        # self.postfix = postfix

    def send_mail(self, to_list, sub, content):
        # me = self.user + "@" + self.postfix
        msg = MIMEText(content, _subtype='html', _charset='utf-8')  # 三个参数：文本内容，文本格式，设置编码
        # msg 是字符串，表示邮件。一般由标题，发信人，收件人，邮件内容，附件等构成，发送邮件的时候，要注意 msg 的格式。
        # 这个格式就是 smtp 协议中定义的格式
        msg['Subject'] = sub  # 邮件title
        # msg['From'] = me
        msg['From'] = self.user  # 发送者
        msg['To'] = ";".join(to_list)  # 接收人邮箱
        try:
            s = smtplib.SMTP()
            s.connect(self.host)  # SMTP 服务器主机
            s.login(self.user, self.pwd)  # 登录，如果是自己的邮箱，则是第三方的stmp服务访问
            # s.sendmail(me, to_list, msg.as_string())
            s.sendmail(self.user, to_list, msg.as_string())
            s.close()
            return True
        except Exception as e:
            print(str(e))
            return False


if __name__ == "__main__":
    SendMail().send_mail(["接收者邮箱"], "测试报告", "msg")