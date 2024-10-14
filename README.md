# Expense Tracker Web Application

## Overview

This is a full-stack **Expense Tracker Web Application** designed to help users manage and monitor their personal expenses effectively. With easy-to-use interfaces and features for categorizing, planning, and monitoring expenses, this application ensures users stay on top of their budgets.

The application is developed using the following technologies:
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript, React.js
- **Database**: SQLite

## Features

- **Manual Expense Entry**: Users can manually add expenses and track their spending.
- **General Expenses**: Provides an overview of all expenses, with an option to split them by time periods (monthly, yearly, etc.).
- **Budget Management**: Set a monthly budget threshold and receive alerts when your spending gets close to the limit.
- **Expense Categorization**: Categorize expenses for a clearer breakdown of where your money is going.
- **Planned Expenses**: Add planned expenses to your monthly budget for better forecasting.
- **Subscription Management**: Add recurring expenses such as subscriptions (monthly, yearly) and have them automatically calculated into your total expenses.

## Architecture

The architecture follows a structured web application design, which includes:

1. **Frontend**: Built with **React.js**, providing a responsive and user-friendly interface. Users can interact with their expense data and access features like expense entry, budgeting, and alerts.
   
2. **Backend**: Developed using **Django**, handling business logic and serving APIs to the frontend. The backend also manages user authentication and data processing.

3. **Database**: Using **SQLite**, a lightweight SQL database, to store user data including expenses, categories, and budget limits.
