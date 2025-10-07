def getTemplate(blogURL, blogImgURL, blogTitle, date):
    return f"""           
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1" />
    <title>{blogTitle}</title>
    <style>
      body {{ margin: 0; padding: 0; -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; }}
      table {{ border-spacing: 0; }}
      img {{ display: block; border: 0; outline: none; text-decoration: none; -ms-interpolation-mode: bicubic; }}
      a {{ color: inherit; text-decoration: none; }}
      @media only screen and (max-width: 600px) {{
        .container {{ width: 100% !important; }}
        .stack {{ display: block !important; width: 100% !important; }}
        .hide-mobile {{ display: none !important; }}
      }}
    </style>
  </head>
  <body style="background-color: #f4f4f6; margin: 0; padding: 20px">
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="max-width: 800px; margin: 0 auto">
      <tr>
        <td align="center">
          <table role="presentation" class="container" width="600" cellpadding="0" cellspacing="0" style="background: #ffffff; border-radius: 8px; overflow: hidden; width: 600px;">
            
            <!-- Logo + Blog name -->
            <tr>
              <td align="center" style="padding:20px; vertical-align:middle;">
                <img src="https://firebasestorage.googleapis.com/v0/b/codeverse-chronicles.appspot.com/o/logo.png?alt=media&token=868aa706-8e9e-4a8e-92c1-83c94c792ff0" alt="Blog Logo" width="80" style="display:inline-block;vertical-align:middle;">
                <span style="font-family:Arial,Helvetica,sans-serif; font-size:20px; font-weight:bold; color:#111827; margin-left:10px; display:inline-block; vertical-align:middle;">
                  CODEVERSE CHRONICLES
                </span>
              </td>
            </tr>

            <!-- Header -->
            <tr>
              <td style="padding: 18px 24px 8px 24px; font-family: Arial, Helvetica, sans-serif; font-size: 14px; color: #6b7280;">
                <strong style="font-size: 16px; color: #111827">Latest article on the Blog</strong>
              </td>
            </tr>

            <!-- Image -->
            <tr>
              <td style="padding: 0 24px 0 24px">
                <a href="{blogURL}" target="_blank" style="display:block;" clicktracking="off">
                  <img src="{blogImgURL}" alt="Blog preview image" width="552" style="width:100%; max-width:552px; height:auto; border-radius:6px;" />
                </a>
              </td>
            </tr>

            <!-- Title -->
            <tr>
              <td style="padding: 16px 24px 8px 24px; font-family: Arial, Helvetica, sans-serif;">
                <a href="{blogURL}" target="_blank" style="text-decoration:none;" clicktracking="off">
                  <h1 style="margin:0; font-size:20px; line-height:1.25; color:#0f172a; font-weight:600;">
                    {blogTitle}
                  </h1>
                </a>
                <p style="margin:12px 0 0 0; color:#374151; font-size:15px; line-height:1.5;">
                  Checkout the latest article exclusively on <strong>Codeverse Chronicles</strong>
                </p>
              </td>
            </tr>

            <!-- Meta -->
            <tr>
              <td style="padding:12px 24px 0 24px; font-family:Arial,Helvetica,sans-serif; color:#6b7280; font-size:13px;">
                By <strong style="color:#111827;">Sandeep Prabhakula</strong> &middot; <span>{date}</span>
              </td>
            </tr>

            <!-- CTA -->
            <tr>
              <td style="padding:18px 24px 24px 24px;">
                <table role="presentation" cellpadding="0" cellspacing="0">
                  <tr>
                    <td align="center" bgcolor="#2563eb" style="border-radius:6px;">
                      <a href="{blogURL}" target="_blank" style="display:inline-block; padding:12px 22px; font-family:Arial,Helvetica,sans-serif; color:#ffffff; font-size:15px; font-weight:600; border-radius:6px;" clicktracking="off">
                        Read the full post
                      </a>
                    </td>
                  </tr>
                </table>
                <p style="margin:12px 0 0 0; font-family:Arial,Helvetica,sans-serif; font-size:13px; color:#6b7280;">
                  Or open in browser: <a href="{blogURL}" target="_blank" style="color:#2563eb;" clicktracking="off">Click here</a>
                </p>
              </td>
            </tr>

            <!-- Separator -->
            <tr>
              <td style="padding:0 24px;">
                <hr style="border:none; border-top:1px solid #eef2f7; margin:0;" />
              </td>
            </tr>
          </table>

          <!-- Inbox preview text -->
          <div style="display:none; white-space:nowrap; font:15px/1px monospace; color:#ffffff; max-height:0; overflow:hidden;">
            {blogTitle} – Read now on Codeverse Chronicles
          </div>
        </td>
      </tr>
    </table>
  </body>
</html>"""
