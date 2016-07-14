#!/usr/bin/python
#coding: utf-8
import imaplib
conn = imaplib.IMAP4_SSL("imap-mail.outlook.com",993)
conn.login("@hotmail.com","")
conn.select("INBOX")
type,data = conn.search(None, 'ALL')
