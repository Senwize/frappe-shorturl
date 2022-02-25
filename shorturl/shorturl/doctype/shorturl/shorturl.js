// Copyright (c) 2022, Senwize B.V. and contributors
// For license information, please see license.txt

const characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
function random_code(length) {
  let code = ""
  for(let i=0; i <length; i++) {
    code += characters[Math.floor(Math.random() * characters.length)]
  }
  return code
}

frappe.ui.form.on('ShortURL', {
  refresh(frm) {
    if (!!frm.doc.short_id) {
      frm.page.set_primary_action(
        "Update Link",
        () => {
          // Verify
          frappe.confirm(
            "You are editing an existing Short Link, which might attached to products (as QR-Code). Are you sure you want to continue?",
            // On "yes": Save form
            () => {
              frm.save()
            },
            // On "cancel": Do nothing
            () => {}
          )
        }
      )
    }
    let template = '<img src="' + frm.doc.qr_code + '" width="240px"/>';
    frm.set_df_property('qr_preview', 'options', frappe.render_template(template));
    frm.refresh_field('qr_preview');
  },
  onload(frm) {
    let template = '<img src="' + frm.doc.qr_code + '" width="240px"/>';
    frm.set_df_property('qr_preview', 'options', frappe.render_template(template));
    frm.refresh_field('qr_preview');
  }
});