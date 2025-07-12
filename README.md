---

<h1 align="center">🔄 Skill Swap Platform</h1>

<p align="center">
  A full-stack application where users can exchange skills with others. Built with <strong>Node.js</strong>, <strong>MongoDB</strong>, <strong>React</strong>, and <strong>Tailwind CSS</strong>.
</p>

---

## 📂 Table of Contents

* [📌 Features](#-features)
* [🛠️ Tech Stack](#-tech-stack)
* [⚙️ Installation](#%ef%b8%8f-installation)
* [🔐 Environment Variables](#-environment-variables)
* [📂 Project Structure](#-project-structure)
* [🛠️ API Endpoints](#%ef%b8%8f-api-endpoints)
* [🧪 Postman Testing](#-postman-testing)
* [👨‍💼 Admin Features](#-admin-features)
* [👥 Team](#-team)
* [🚀 Deployment Ready](#-deployment-ready)

---

## 📌 Features

### 👤 User Features

* Register & Login with JWT
* Manage Profile (name, location, skills, etc.)
* Toggle Public/Private profile
* Search users by skill
* Send, accept, reject, delete skill swap requests
* One-time feedback submission

### 🚮 Admin Features

* Ban/Unban Users
* View all swaps and feedback
* Platform announcements
* Export activity reports (CSV)

---

## 🛠️ Tech Stack

### Backend:

* **Node.js + Express**
* **MongoDB + Mongoose**
* **JWT + Bcrypt**
* **Nodemon**, **json2csv**

### Frontend:

* **React + Vite + TypeScript**
* **Tailwind CSS + shadcn-ui**
* **Axios**, **React Router DOM**

---

## ⚙️ Installation

### Backend:

```bash
git clone https://github.com/sayout-de003/SkillSwap.git
cd skill-swap-backend
npm install
```

### Frontend:

```bash
cd ../frontend
npm install
```

---

## 🔐 Environment Variables

### Backend `.env`

```env
MONGO_URI=mongodb://localhost:27017/skill-swap
JWT_SECRET=your_jwt_secret
PORT=5000
```

### Frontend `.env`

```env
VITE_API_URL=http://localhost:5000
```

---

## 📂 Project Structure

```
project-root/
├── backend/
│   ├── controllers/
│   ├── models/
│   ├── routes/
│   ├── middlewares/
│   ├── utils/
│   ├── config/
│   ├── app.js
│   └── server.js
├── frontend/
│   ├── public/
│   └── src/
│       ├── components/
│       ├── pages/
│       ├── hooks/
│       └── App.tsx
```

---

## 🛠️ API Endpoints

### 🔐 Auth

| Method | Endpoint           | Description     |
| ------ | ------------------ | --------------- |
| POST   | /api/auth/register | Register a user |
| POST   | /api/auth/login    | Login & get JWT |

### 👤 User Profile

| Method | Endpoint          | Description                 |
| ------ | ----------------- | --------------------------- |
| GET    | /api/users/me     | Get logged-in user profile  |
| PUT    | /api/users/me     | Update own profile          |
| GET    | /api/users/public | Search public user profiles |

### 🔄 Swap Requests

| Method | Endpoint               | Description             |
| ------ | ---------------------- | ----------------------- |
| POST   | /api/swaps/request     | Create swap request     |
| PUT    | /api/swaps/\:id/accept | Accept swap request     |
| PUT    | /api/swaps/\:id/reject | Reject swap request     |
| DELETE | /api/swaps/\:id        | Delete swap (own)       |
| GET    | /api/swaps/me          | Get sent/received swaps |

### 🌟 Feedback

| Method | Endpoint                   | Description          |
| ------ | -------------------------- | -------------------- |
| POST   | /api/ratings/\:swapId      | Submit feedback      |
| GET    | /api/ratings/user/\:userId | Get feedback of user |

---

## 🧪 Postman Testing

### 1. Register & Login

```http
POST /api/auth/register
POST /api/auth/login
```

### 2. Profile APIs

```http
GET /api/users/me
PUT /api/users/me
```

### 3. Search Public Users

```http
GET /api/users/public?skill=Excel
```

### 4. Swap APIs

```http
POST /api/swaps/request
PUT /api/swaps/:id/accept
PUT /api/swaps/:id/reject
DELETE /api/swaps/:id
GET /api/swaps/me
```

### 5. Feedback

```http
POST /api/ratings/:swapId
GET /api/ratings/user/:userId
```

### 6. Admin APIs

```http
POST /api/admin/ban/:userId
GET /api/admin/swaps
GET /api/admin/feedback
POST /api/admin/announce
GET /api/admin/report/users
```

<h3 align="center">🧪 Postman Preview</h3>
<p align="center">
  <img src="https://i.ibb.co/CKZqb54H/odooo.jpg" width="500"/>
</p>

---

## 👥 Team

<table align="center">
  <tr>
    <td align="center">
      <img src="https://github.com/sayout-de003.png" width="100"><br>
      <strong>Sayantan De</strong><br>
      <a href="https://github.com/sayout-de003">@sayout-de003</a>
    </td>
    <td align="center">
      <img src="https://github.com/himasnhu018.png" width="100"><br>
      <strong>Himanshu Kumar Gupta</strong><br>
      <a href="https://github.com/himasnhu018">@himasnhu018</a>
    </td>
    <td align="center">
      <img src="https://github.com/Satyaamp.png" width="100"><br>
      <strong>Satyam Kumar</strong><br>
      <a href="https://github.com/Satyaamp">@Satyaamp</a>
    </td>
  </tr>
</table>

---

## 🚀 Deployment Ready

You can deploy the platform easily using:

* ✨ [Render](https://render.com)
* ⚡ [Railway](https://railway.app)
* ☁️ [Vercel](https://vercel.com) (Frontend)

Supports `.env`, MongoDB Atlas, and REST tools like Postman, Thunder Client, or Axios.


---
