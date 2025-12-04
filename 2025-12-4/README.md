```markdown
<h1 align="center">dpl_devops_training</h1>

<h3 align="center" style="color:#007bff;">Daily DevOps Practice • TypeScript Basics • Personal Project</h3>

---

## 🎯 Objective Recap
- **Read the TypeScript handbook** (basic & everyday types) and practice with a small TypeScript project.
- **Watch and follow** a TypeScript-focused tutorial to understand typing, unions, literal types and arrays.
- **Create a simple TypeScript project** to apply learnings and capture notes/screenshots.

> Today I focused on TypeScript fundamentals and building a small project to practice types and basic typings.

---

## 🛠️ Study Environment
- **Host OS:** Windows
- **Editor:** Visual Studio Code
- **Terminal:** PowerShell (Windows PowerShell v5.1)
- **Notes & Evidence:** images placed in `2025-12-4/images/` and referenced below

---

## 📚 Study Sources

- **TypeScript Handbook (Basics):** https://www.typescriptlang.org/docs/handbook/2/basic-types.html
- **YouTube tutorial watched:** https://www.youtube.com/watch?v=SpwzRDUQ1GI

⭐️ Course Contents ⭐️
0:00:00 Introduction
0:06:39 Intro to Pizza app
0:16:49 Move code to TS
0:19:58 Defensive coding
0:24:36 Obligatory types basics lesson
0:28:29 Add type to orderId
0:29:55 Defining Custom Types
0:33:44 Adding a Pizza type
0:38:00 Nested object types
0:43:15 Optional properties
0:45:58 Adding an Order type
0:47:20 Typing arrays
0:52:00 Type orderQueue
0:56:13 Literal types
0:58:57 Unions
1:01:57 Update order status to use literal type unions

Watched all this from the linked YouTube video above.

---

## 🧩 Project: TypeScript Practice

I created a small TypeScript project today to get hands-on experience with typing, unions, arrays, and custom types. I used several AI tools to accelerate scaffolding and get suggestions for types and function signatures.

- **What I implemented:**
  - Converted a simple Pizza-order example to TypeScript
  - Added custom types for `Pizza`, `Order`, and `OrderStatus` (literal unions)
  - Typed arrays and nested objects
  - Defensive checks using union types and optional properties

- **Artifacts:** Project files and working snippets are stored in this folder. Supporting screenshots and images are in `images/`.

---

## 🔎 Key Learnings

- TypeScript's basic types (`string`, `number`, `boolean`) are simple but powerful when combined with unions and type aliases.
- Literal type unions are useful for constrained status values (e.g., `"pending" | "done"`).
- Typing arrays and nested objects makes code safer and easier to refactor.
- AI tools can speed up scaffolding but review types carefully.

---

## ✅ Evidence / Next Steps

- Screenshots added in `2025-12-4/images/` (please review images for terminal output and sample code snapshots).
- Next: expand the project to add small tests and type guards; refactor to strip `any` usages.

---

**Daily summary:** Read TypeScript basics, watched a practical TS tutorial (timestamps above), and built a small TypeScript practice project using AI-assisted scaffolding. Files and images are included in this folder.

Made by Sufi Hassan Asim — 2025-12-04
```

---

## 🏷️ Project: Meeting Room Booker (room-booker-dpl)

I also worked on a separate project — *Meeting Room Booker* — and included its README content and screenshots here for reference. The app is live and the source code is available at the links below.

- Live app: https://room-booker-dpl.vercel.app/
- GitHub repo: https://github.com/Hassan-asim/room-booker-dpl

### Demo & Screenshots
Banner and app screenshots (served from this folder):

![banner](./images/banner.png)
![logo](./images/logo.png)
![ss1](./images/ss1.png)
![ss2](./images/ss2.png)
![ss3](./images/ss3.png)
![ss4](./images/ss4.png)
![ss5](./images/ss5.png)
![ss6](./images/ss6.png)
![ss7](./images/ss7.png)

### Quick Project Summary

Meeting Room Booker is a production-ready meeting room booking system with a React + TypeScript frontend and a Node.js + Express backend (Prisma + SQLite for local development). It supports an interactive calendar (FullCalendar), real-time updates via Socket.IO, an admin panel with JWT auth, PWA installability, and responsive UI with dark mode.

Key highlights:
- Interactive calendar with day/week/month views
- Real-time bookings using Socket.IO
- Admin CRUD for rooms and bookings
- Prevents double bookings and validates capacity/time
- PWA support (service worker + manifest)

### Tech Stack
- Frontend: React 18, TypeScript, Vite, Tailwind CSS, Ant Design, FullCalendar
- Backend: Node.js, Express, Prisma (SQLite for local dev)
- Realtime: Socket.IO
- PWA: vite-plugin-pwa

### Getting Started (local)

Prerequisites: Node.js 18+ and npm

Install & run:

```powershell
npm install
cd server
npm install
cd ..
cd server
npx prisma db push
npx ts-node seed.ts
cd ..
# In terminal 1 (backend)
cd server; npm run dev
# In terminal 2 (frontend)
npm run dev
```

Open the app at `http://localhost:8080` (admin panel at `/admin` when seeded).

### API Endpoints (summary)
- `POST /api/bookings` - Create a new booking
- `GET /api/bookings` - Get bookings (with filters)
- Admin (JWT required): `POST /api/admin/login`, `POST /api/admin/rooms`, `PUT /api/admin/rooms/:id`, `DELETE /api/admin/rooms/:id`, `GET /api/admin/bookings`, `PUT /api/admin/bookings/:id/end`

### Project Structure (short)
```
room-booker-dpl/
├── src/                      # Frontend source
├── server/                   # Backend source (Prisma, seed, API)
└── public/                   # Static assets + screenshots
```

For full project details, see the repository: https://github.com/Hassan-asim/room-booker-dpl

