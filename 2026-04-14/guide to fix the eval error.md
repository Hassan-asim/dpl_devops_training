Here is a **complete, clean, copy-paste-ready Markdown file** with everything structured simply and clearly:

---

```md
# 🛠️ Fix Guide: App Loads Without Styling (CSP Issue)

---

## 🎯 Problem Summary

After deployment:
- App loads as plain HTML (no styling)
- UI looks broken (no CSS/Tailwind applied)
- Images and API calls may still work

### Console Error:
```

Refused to evaluate a string as JavaScript because 'unsafe-eval' is not allowed

```

---

## ✅ Root Cause

The **Content Security Policy (CSP)** is too strict and is **blocking JavaScript execution**.

This prevents:
- React hydration
- Next.js runtime execution
- Tailwind CSS from applying correctly

---

## 🔍 Step 1 — Confirm the Issue

1. Open the app in browser
2. Press `F12`
3. Go to **Console tab**
4. Look for error:
```

unsafe-eval is not allowed

````

If you see this → continue

---

## 🔍 Step 2 — Find Where CSP is Set

CSP can be defined in multiple places. Check all of the following:

---

### 🔹 Option A — NGINX (Most Common)

Connect to the server (via SSH or AWS SSM):

```bash
sudo cat /etc/nginx/sites-enabled/default
````

OR:

```bash
sudo cat /etc/nginx/nginx.conf
```

Look for:

```nginx
add_header Content-Security-Policy ...
```

---

### 🔹 Option B — Next.js Configuration

Check:

```bash
cat next.config.js
```

Look for something like:

```js
async headers() {
  return [
    {
      source: "/(.*)",
      headers: [
        {
          key: "Content-Security-Policy",
          value: "..."
        }
      ]
    }
  ];
}
```

---

### 🔹 Option C — Cloudflare (Very Likely)

If Cloudflare is being used:

1. Open Cloudflare Dashboard
2. Select your domain
3. Go to:

   * **Security**
   * **Rules**
   * **Transform Rules / Response Headers**
4. Look for `Content-Security-Policy`

---

## 🔧 Step 3 — Apply the Fix

### ✅ Temporary Fix (For QA Environment)

Update CSP to allow JavaScript execution:

```
'unsafe-eval' 'unsafe-inline'
```

---

### ✔ Fix in NGINX

Update config:

```nginx
add_header Content-Security-Policy "script-src 'self' 'unsafe-eval' 'unsafe-inline' https:;";
```

Then restart NGINX:

```bash
sudo systemctl restart nginx
```

---

### ✔ Fix in Next.js

Update CSP in `next.config.js`:

```js
{
  key: "Content-Security-Policy",
  value: "script-src 'self' 'unsafe-eval' 'unsafe-inline';"
}
```

Then rebuild and restart:

```bash
npm run build
pm2 restart all
```

---

### ✔ Fix in Cloudflare

Set or update header:

```
Content-Security-Policy: script-src 'self' 'unsafe-eval' 'unsafe-inline' https:;
```

---

## 🔄 Step 4 — Restart Services

Run:

```bash
pm2 restart all
sudo systemctl restart nginx
```

---

## 🔄 Step 5 — Verify Fix

1. Open the application
2. Hard refresh:

   ```
   Ctrl + Shift + R
   ```
3. Check:

   * UI styling is restored
   * No CSP errors in console

---

## ✅ Expected Result

* App loads correctly with full styling
* React hydration works
* No console errors

---

## ⚠️ Important Note (Production)

This fix allows:

```
unsafe-eval
unsafe-inline
```

👉 These are **NOT recommended for production**

For production:

* CSP should be stricter
* Use nonce/hash-based policies instead

---

## 🚀 Summary

| Component     | Status        |
| ------------- | ------------- |
| Build         | ✅ OK          |
| Deployment    | ✅ OK          |
| Static Assets | ✅ OK          |
| CSP Policy    | ❌ Blocking JS |

👉 Fixing CSP resolves the issue completely

---

```

---

This is ready to:
- paste in Slack
- attach in Jira
- share with your dev directly

If you want, I can also give you a **production-grade CSP config** next.
```
