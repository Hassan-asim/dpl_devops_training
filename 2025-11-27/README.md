<h1 align="center">dpl_devops_training</h1>

<h3 align="center" style="color:#00a86b;">Daily DevOps Practice • NGINX Deep Dive • Load Balancing</h3>

---

## 🎧 Study Log – NGINX Complete Tutorial

Today I completed the full **NGINX Crash Course** ([YouTube](https://www.youtube.com/watch?v=9t9Mp0BGnyI)). Topics covered:

| Timestamp | Topic |
|-----------|-------|
| ⌨️ (00:00) | What is NGINX |
| ⌨️ (08:18) | NGINX Installation |
| ⌨️ (11:11) | NGINX Terminology |
| ⌨️ (13:16) | Serving Static Content |
| ⌨️ (17:34) | Mime Types |
| ⌨️ (22:48) | Location Context |
| ⌨️ (33:16) | Rewrites and Redirect |
| ⌨️ (37:53) | NGINX as a Load Balancer |

---

## 🔧 NGINX Installation

### Installing NGINX on Ubuntu

Following the official NGINX release documentation, I installed NGINX on the Ubuntu system using the terminal.

![Installing NGINX using docs](images/installing%20the%20ngenx%20using%20the%20relese%20docs%20provided%20on%20the%20ubuntu%20system%20.png)

![Running installation commands](images/installing%20the%20ngenx%20using%20the%20relese%20docs%20provided%20on%20the%20ubuntu%20system%20by%20running%20all%20the%20commands%20using%20the%20terminal%20of%20ubuntu.png)

### Installation Complete

Successfully installed NGINX and got it running on the local server.

![NGINX being installed](images/nginx%20being%20installed.png)

![NGINX running on local server](images/nginx%20installed%20and%20executed%20on%20local%20server.png)

### Verification

Verified through the browser's console network output that the server is actually running NGINX.

![Verifying NGINX in console](images/varifying%20through%20consol%20network%20output%20that%20the%20server%20is%20actually%20nginx%20.png)

---

## 📄 Serving Static Content

### Creating Static HTML Page

Created a static HTML page called `index.html` to practice NGINX configuration.

![Creating static HTML page](images/made%20a%20static%20html%20page%20called%20index.htm%20to%20practice%20teh%20nginx%20.png)

### Configuring NGINX

Configured the `nginx.conf` file to serve the static page locally.

![Configuring nginx.conf](images/configuaring%20the%20nginx%20conf%20file%20to%20serve%20mt%20static%20page%20locally.png)

### Setting Permissions

Set the permissions of the `mySite` folder to global so NGINX can access and serve the site.

![Setting folder permissions](images/setting%20the%20permission%20of%20the%20folder%20mySite%20to%20global%20so%20the%20ngnix%20can%20have%20access%20to%20get%20the%20site%20.png)

### Successfully Serving Static Page

Successfully served the static page using NGINX in Ubuntu and verified through console that it's being served by the NGINX server.

![Static page served](images/successfully%20served%20a%20static%20page%20using%20ngnix%20in%20ubuntu%20%20%20and%20varifying%20its%20status%20from%20the%20consol%20that%20it%20is%20being%20served%20by%20teh%20ngnix%20server.png)

![Root static page](images/root%20static%20page.png)

---

## 🎨 Mime Types

### CSS File Serving Issue

Initially, the CSS file was being served but fetched as a plain text file instead of a CSS file for styling.

![CSS as plain text](images/successfully%20served%20a%20static%20page%20but%20with%20a%20css%20style%20file%20%20using%20nginx%20in%20ubuntu%20%20%20and%20varifying%20its%20status%20from%20the%20consol%20that%20the%20css%20file%20is%20being%20served%20but%20is%20being%20fetched%20as%20a%20plain%20txt%20file%20.png)

### Fixing Mime Types

After configuring the correct mime types, the CSS file is now being fetched properly as a CSS file for styling.

![CSS properly served](images/successfully%20served%20a%20static%20page%20but%20with%20a%20css%20style%20file%20%20using%20nginx%20in%20ubuntu%20%20%20and%20varifying%20its%20status%20from%20the%20consol%20that%20the%20css%20file%20is%20being%20served%20but%20is%20being%20fetched%20as%20a%20CSS%20file%20for%20styling%20.png)

---

## 📍 Location Context & Try Files

### Creating Multiple Pages

Created a new folder called `info` with a `devops` page. This was challenging due to permission and type errors for CSS and PNG files.

![Creating info folder and devops page](images/now%20amke%20a%20new%20folder%20called%20info%20and%20make%20a%20new%20page%20devops%20and%20tried%20to%20serve%20it%20using%20teh%20tryf%20files%20directive%20it%20was%20challenging%20had%20a%20lot%20of%20issues%20with%20permission%20and%20types%20error%20for%20the%20css%20file%20and%20png%20file.png)

### Using Try Files Directive

Successfully served the static page with CSS using the `try_files` directive.

![Try files with CSS](images/successfully%20served%20a%20static%20page%20but%20with%20a%20css%20style%20file%20and%20a%20try%20files%20directive%20%20using%20nginx%20in%20ubuntu%20%20%20and%20varifying%20its%20status%20from%20the%20consol%20that%20the%20css%20file%20is%20being%20served%20but%20is%20being%20fetched%20as%20a%20CSS%20file%20for%20styling%20.png)

![Try files success](images/successfully%20served%20a%20static%20page%20but%20with%20a%20css%20style%20file%20and%20teh%20try%20files%20directive%20%20using%20nginx%20in%20ubuntu%20%20%20and%20varifying%20its%20status%20from%20the%20consol%20that%20the%20css%20file%20is%20being%20served%20but%20is%20being%20fetched%20as%20a%20CSS%20file%20for%20styling.png)

### Serving New Static Page

Successfully served the new static page using the `try_files` directive.

![New static page with try_files](images/successfully%20served%20teh%20new%20static%20page%20using%20teh%20try%20files%20directive.png)

![DevOps page](images/devops%20page%20.png)

### Using Alias Directive

Used the `alias` directive in the NGINX config file to access the profile page via multiple addresses – having 2 different URIs to access the same page.

![Using alias directive](images/using%20alies%20directive%20in%20the%20mginx%20config%20file%20to%20assess%20the%20profine%20page%20in%20teh%20nginx%20server%20like%20having%202%20different%20address%20to%20access%20the%20same%20page%20.png)

![Profile static page](images/my%20profile%20static%20page%20.png)

![Accessing profile with /me](images/accessing%20the%20same%20profile%20page%20using%20the%20me%20address%20.png)

### Regular Expressions in Location

Set up regex expressions in the config file to access the devops page using multiple different addresses.

![Regex in config](images/setting%20the%20regex%20expression%20in%20the%20confg%20file%20to%20access%20the%20devops%20page%20usin%20new%20multitude%20of%20addresses.png)

![Accessing with regex URI](images/accessing%20the%20devops%20info%20page%20using%20teh%20new%20uri%20using%20teh%20regular%20expression%20.png)

---

## 🔄 Rewrites and Redirects

### Redirect with Return 307

Used the `return 307` directive to redirect the `/devops` URI to the info page.

![Redirect with return 307](images/using%20teh%20concept%20or%20redirect%20to%20redirect%20the%20devops%20uri%20to%20the%20info%20page%20usingteh%20return%20307%20%20directive.png)

### Rewrite Directive

Used the `rewrite` directive to redirect the `/devops` URI to the info page while keeping `/devops` in the URL.

![Rewrite directive](images/using%20teh%20concept%20or%20rewrite%20to%20redirect%20the%20devops%20uri%20to%20the%20info%20page%20%20while%20keepingthe%20devops%20in%20teh%20url%20using%20teh%20rewrite%20%20directive.png)

---

## ⚖️ NGINX as a Load Balancer

### Installing Docker

Installed Docker to create multiple server instances for testing NGINX load balancing.

![Installing Docker](images/installing%20Docker%20to%20test%20the%20lode%20balencer%20of%20the%20nginx%20.png)

### Configuring Load Balancing

Modified the NGINX config file and access log to use load balancing with Docker containers as backend servers.

![Load balancing config](images/access%20log%20and%20config%20file%20changed%20to%20use%20load%20balancing%20in%20nginx%20using%20docker%20for%20server.png)

### Load Balancing Success

Successfully ran the load balancing exercise using Docker containers to create 4 different servers, with NGINX distributing traffic between them.

![Load balancing success](images/successfully%20ran%20the%20loadbalancing%20exercise%20using%20the%20docker%20container%20to%20create%20the%204%20diff%20server%20.png)

---

## 📝 Key Concepts Learned

### NGINX Terminology
- **Directives**: Configuration instructions in NGINX
- **Contexts**: Blocks that group directives (http, server, location)
- **Upstream**: Backend server pool for load balancing

### Important Directives
- `root` – Sets the root directory for requests
- `index` – Defines default files to serve
- `try_files` – Tries serving files in order, falls back to last option
- `alias` – Maps URI to different filesystem path
- `return` – Returns specific status code and redirects
- `rewrite` – Rewrites URI while keeping original URL visible
- `proxy_pass` – Forwards requests to upstream servers

### Load Balancing Methods
- **Round Robin** (default) – Distributes requests evenly
- **Least Connections** – Sends to server with fewest connections
- **IP Hash** – Routes based on client IP for session persistence

---

## 🗂️ Reference Assets & Next Steps

- `images/` – 28 screenshots documenting the complete NGINX tutorial journey

Next session I will:

1. Explore NGINX reverse proxy configuration in depth
2. Set up HTTPS/SSL with NGINX
3. Practice NGINX with real application deployment
4. Continue with advanced load balancing strategies

---

## 📚 References

- [NGINX Crash Course - Full Tutorial](https://www.youtube.com/watch?v=9t9Mp0BGnyI)
- [NGINX Official Documentation](https://nginx.org/en/docs/)


