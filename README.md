
---

# 🔄 Skill Swap Platform — Backend

A full-featured backend API for a **Skill Swap Platform**, where users can list the skills they offer and want, send/receive swap requests, provide feedback after swaps, and interact with an admin-moderated system.

---

## 📚 Table of Contents

- [📌 Features](#-features)
- [🧰 Tech Stack](#-tech-stack)
- [⚙️ Installation](#️-installation)
- [🔐 Environment Variables](#-environment-variables)
- [📂 Project Structure](#-project-structure)
- [🛠️ API Endpoints](#️-api-endpoints)
- [🧪 Postman Testing](#-postman-testing)
- [👨‍💻 Admin Features](#-admin-features)
- [👥 Team](#-team)
- [🚀 Deployment Ready](#-deployment-ready)

---

## 📌 Features

### 👤 User Features
- Register, login, JWT-based auth
- Update profile (name, location, photo, availability, skills)
- Set profile as public or private
- Browse/search users by skill
- Send, accept, reject, or delete skill swap requests
- Track pending/accepted swaps
- Submit one-time feedback after a swap

### 👮 Admin Features
- View and ban/unban users
- Monitor all swaps and feedback
- Send platform-wide announcements
- Download activity reports (CSV)

---

## 🧰 Tech Stack

- **Node.js + Express** (API framework)
- **MongoDB + Mongoose** (database & ODM)
- **JWT + Bcrypt** (auth & security)
- **Nodemon** (dev hot reload)
- **Postman** (API testing)
- **json2csv** (CSV report generation)

---

## ⚙️ Installation

1. **Clone the repo**
```bash
git clone https://github.com/your-username/skill-swap.git
cd skill-swap-backend
````

2. **Install dependencies**

```bash
npm install
```

3. **Create `.env` file**

```env
MONGO_URI=mongodb://localhost:27017/skill-swap
JWT_SECRET=your_jwt_secret
PORT=5000
```

4. **Run server**

```bash
npm run dev
```

---

## 📂 Project Structure

```
skill-swap-backend/
├── controllers/
├── models/
├── routes/
├── middlewares/
├── utils/
├── config/
├── app.js
├── server.js
├── .env
└── README.md
```

---

## 🛠️ API Endpoints

### 🔐 Auth

| Method | Endpoint             | Description         |
| ------ | -------------------- | ------------------- |
| POST   | `/api/auth/register` | Register a new user |
| POST   | `/api/auth/login`    | Login and get token |

---

### 👤 User Profile

| Method | Endpoint            | Description                     |
| ------ | ------------------- | ------------------------------- |
| GET    | `/api/users/me`     | Get own profile                 |
| PUT    | `/api/users/me`     | Update profile                  |
| GET    | `/api/users/public` | Search public profiles by skill |

---

### 🔄 Swap Requests

| Method | Endpoint                | Description                  |
| ------ | ----------------------- | ---------------------------- |
| POST   | `/api/swaps/request`    | Send a swap request          |
| PUT    | `/api/swaps/:id/accept` | Accept a swap                |
| PUT    | `/api/swaps/:id/reject` | Reject a swap                |
| DELETE | `/api/swaps/:id`        | Delete own pending swap      |
| GET    | `/api/swaps/me`         | Get my swaps (sent/received) |

---

### 🌟 Feedback / Ratings

| Method | Endpoint                    | Description               |
| ------ | --------------------------- | ------------------------- |
| POST   | `/api/ratings/:swapId`      | Submit feedback post-swap |
| GET    | `/api/ratings/user/:userId` | View ratings for a user   |

---

## 👨‍💻 Admin Features (Requires Admin Token)

| Method | Endpoint                  | Description                       |
| ------ | ------------------------- | --------------------------------- |
| POST   | `/api/admin/ban/:userId`  | Ban or unban a user               |
| GET    | `/api/admin/swaps`        | View all swap requests            |
| GET    | `/api/admin/feedback`     | View all feedback logs            |
| POST   | `/api/admin/announce`     | Send platform-wide announcement   |
| GET    | `/api/admin/report/:type` | Download report (users, swaps...) |

---

## 🧪 Postman Testing

### 1. ✅ Register & Login

* `POST /api/auth/register`
* `POST /api/auth/login` → get JWT

### 2. 👤 Profile

* `GET /api/users/me` (auth required)
* `PUT /api/users/me` (update skills, location...)

### 3. 🔍 Search Public Profiles

* `GET /api/users/public?skill=Excel`

### 4. 🤝 Swap System

* `POST /api/swaps/request`
* `PUT /api/swaps/:id/accept`, `reject`
* `DELETE /api/swaps/:id`
* `GET /api/swaps/me`

### 5. 🌟 Feedback

* `POST /api/ratings/:swapId`
* `GET /api/ratings/user/:userId`

### 6. 👮 Admin (use admin token)

* `POST /api/admin/ban/:userId`
* `GET /api/admin/swaps`
* `GET /api/admin/feedback`
* `POST /api/admin/announce`
* `GET /api/admin/report/users|swaps|feedback`

---

## 👥 Team

* **Sayantan De**
* **Himanshu Kumar Gupta**
* **Satyam Kumar**

---

## 🚀 Deployment Ready

You can easily deploy this backend to:

* 🌐 [Render](https://render.com)
* ⚡ [Railway](https://railway.app)
* ☁️ [Vercel Serverless (Express adapter)](https://vercel.com)

Supports `.env`, MongoDB Atlas, and REST clients like Postman or Axios.


