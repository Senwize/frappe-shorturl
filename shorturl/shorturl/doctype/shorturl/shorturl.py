# Copyright (c) 2022, Senwize B.V. and contributors
# For license information, please see license.txt

# import frappe
from frappe.utils import random_string, get_url
from frappe.website.website_generator import WebsiteGenerator
import frappe

import qrcode
from PIL import Image
import base64
import os
from io import BytesIO


# - Document name (descriptive)
# - Document short_id is the route suffix
# - Document short_url is the full short url
# - Document long_url

def create_qr(url):
  qr = qrcode.QRCode(
      version=1,
  )
  qr.add_data(url)
  img = qr.make_image()
  temp = BytesIO()
  img.save(temp, "PNG")
  temp.seek(0)
  b64 = base64.b64encode(temp.read())
  return "data:image/png;base64,{0}".format(b64.decode("utf-8"))


class ShortURL(WebsiteGenerator):
  def generate_code(self):
    retries = 0
    while retries < 3:
      random_code = random_string(5)
      doc = frappe.get_value("ShortURL", {"short_id": random_code}, "name")
      if doc:
        retries += 1
      else:
        return random_code
    frappe.throw(_("Try again, generated code is repeated on ") + doc.name)

  def before_save(self):
    if self.short_id == "":
      self.short_id = self.generate_code()
    # self.qr_code = get_qrcode(qr_code, self.logo)
    self.route = 'l/' + self.short_id
    url = get_url(self.route)
    self.short_url = url
    self.qr_code = create_qr(url)
