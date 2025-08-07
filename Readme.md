# 🐼 Learn Basic Pandas in 15 Qs

> 🚀 **Master pandas fundamentals through 15 interactive questions and hands-on exercises**

<div align="center">

![Python](https://img.shields.io/badge/Python-3.7+-blue?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Latest-orange?style=flat-square&logo=pandas&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Difficulty](https://img.shields.io/badge/Difficulty-Beginner-brightgreen?style=flat-square)

</div>

---

## 🎯 What You'll Learn

<table>
<tr>
<td>

---

## 📚 Learning Path

### 🏗️ **Foundation** `Questions 1-5`

```
🏁 00. Create Data Frame                    ⭐ Easy
📝 01. Create DataFrame from List           ⭐ Easy  
📏 02. Get DataFrame Size                   ⭐ Easy
👀 03. Display First Three Rows             ⭐ Easy
🎯 04. Select Data                          ⭐ Easy
➕ 05. Create New Column                    ⭐ Easy
```

### 🧽 **Data Cleaning** `Questions 6-11`

```
🗑️ 06. Drop Duplicate Rows                 ⭐ Easy
❌ 07. Drop Missing Data                    ⭐ Easy
✏️ 08. Modify Columns                       ⭐ Easy
🏷️ 09. Rename Columns                       ⭐ Easy
🔄 10. Change Data Type                     ⭐ Easy
🔧 11. Fill Missing Data                    ⭐ Easy
```

### 🔀 **Data Reshaping** `Questions 12-14`

```
📎 12. Concatenate DataFrames               ⭐ Easy
🔄 13. Pivot Tables                         ⭐ Easy
📊 14. Melt Data (Wide to Long)             ⭐ Easy
```

### 🚀 **Advanced Techniques** `Question 15`

```
⛓️ 15. Method Chaining                      ⭐ Easy
```

---

## 🛠️ Quick Start

### ⚡ **1-Minute Setup**

```bash
# 📥 Clone the repository
git clone https://github.com/KanekiEzz/Learn_Basic_Pandas_In_15_Qs.git
cd Learn_Basic_Pandas_In_15_Qs

# 🐍 Create virtual environment  
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 📦 Install dependencies
pip install pandas numpy jupyter matplotlib seaborn
```

### 🎮 **How to Play**

<div align="center">

| Step |        Action        | Description                    |
| :---: | :-------------------: | ------------------------------ |
| 1️⃣ |   **📖 Read**   | Study the problem statement    |
| 2️⃣ |  **💭 Think**  | Plan your approach             |
| 3️⃣ |  **⌨️ Code**  | Implement your solution        |
| 4️⃣ |  **✅ Check**  | Compare with provided solution |
| 5️⃣ | **🔄 Practice** | Try variations and edge cases  |

</div>

---

## 📁 Project Structure

```
🐼 Learn_Basic_Pandas_In_15_Qs/
├── 🏗️ 00.Create_Data_Frame/
├── 📝 01.Create_A_DataFrame_from_List/
├── 📏 02.Get_The_Size_Of_A_DataFrame/
├── 👀 03.Display_The_First_Three_Rows/
├── 🎯 04.Select_Data/
├── ➕ 05.Create_A_New_Column/
├── 🗑️ 06.Drop_Duplicate_Rows/
├── ❌ 07.Drop_Missing_Data/
├── ✏️ 08.Modify_Columns/
├── 🏷️ 09.Rename_Columns/
├── 🔄 10.Change_Data_Type/
├── 🔧 11.Fill_Missing_Data/
├── 📎 12.Reshape_Data:_Concatenate/
├── 🔄 13.Reshape_Data:_Pivot/
├── 📊 14.Reshape_Data:_Melt/
├── ⛓️ 15.Method_Chaining/
├── 🐍 venv/
├── 📄 MIT license
└── 📖 Readme.md
```

---

## 💡 Learning Strategy

<div align="center">

### 🎯 **Your 15-Day Journey**

</div>

|       Week       |           Focus Area           |             Goals             | Time Investment |
| :--------------: | :----------------------------: | :---------------------------: | :-------------: |
| **Week 1** |   🏗️**Foundations**   |    Master basic operations    |  ⏰ 30 min/day  |
| **Week 2** |   🧹**Data Cleaning**   | Handle real-world data issues |  ⏰ 45 min/day  |
| **Week 3** | 🔀**Advanced Reshaping** |   Transform data like a pro   |  ⏰ 60 min/day  |

### 🎨 **Learning Modes**

<table>
<tr>
<td align="center">

---

## 🏆 Skills You'll Master

<div align="center">

| 🛠️**Core Skills** | 🧹**Cleaning Skills** | 🔀**Reshaping Skills** | 🚀**Advanced Skills** |
| :-----------------------: | :-------------------------: | :--------------------------: | :-------------------------: |
|   ✅ DataFrame creation   |  ✅ Missing value handling  |       ✅ Concatenation       |     ✅ Method chaining     |
|    ✅ Data inspection    |    ✅ Duplicate removal    |       ✅ Pivot tables       |    ✅ Code optimization    |
|    ✅ Column selection    |   ✅ Data type conversion   |       ✅ Melting data       |    ✅ Readable pipelines    |
|     ✅ Row filtering     |     ✅ Column renaming     |    ✅ Data transformation    |     ✅ Performance tips     |

</div>

---

## 📊 Sample Datasets

### 🎭 **Variety of Real-World Data**

<div align="center">

|      Dataset Type      |        📝 Description        |    🎯 Use Case    |
| :---------------------: | :--------------------------: | :----------------: |
| 🛒**E-commerce** |  Sales, customers, products  | Business analytics |
|  🎓**Education**  | Student grades, demographics | Academic analysis |
|   💰**Finance**   |  Stock prices, transactions  | Financial modeling |
|   📈**Survey**   | Responses, ratings, feedback | Research analysis |
| ⏰**Time Series** |      Date-indexed data      |   Trend analysis   |

</div>

---

## 🎨 Code Style Guide

### ✨ **Beautiful Pandas Code**

```python
# ❌ Avoid: Nested, hard-to-read code
df_filtered = df[df['age'] > 25]
df_grouped = df_filtered.groupby('category').agg({'sales': 'sum'})
df_sorted = df_grouped.sort_values('sales', ascending=False)

# ✅ Prefer: Clean method chaining  
result = (df
    .query('age > 25')
    .groupby('category')
    .agg({'sales': 'sum'})
    .sort_values('sales', ascending=False)
)
```

---

## 🌟 Success Tips

<table>
<tr>
<td>

---

## 🔗 Helpful Resources

<div align="center">

### 📚 **Essential Links**

|                                        Resource                                        |      Type      |        Description        |
| :-------------------------------------------------------------------------------------: | :-------------: | :-----------------------: |
|               [📖 **Official Docs**](https://pandas.pydata.org/docs/)               |  Documentation  | Complete pandas reference |
|        [📄 **Cheat Sheet**](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)        | Quick Reference | Key functions at a glance |
|              [🎓 **Kaggle Learn**](https://www.kaggle.com/learn/pandas)              |     Course     | Interactive pandas course |
| [📘 **Data Science Handbook**](https://jakevdp.github.io/PythonDataScienceHandbook/) |      Book      |    Comprehensive guide    |

</div>

---

## 🤝 Contributing

### 💡 **Ways to Help**

<table>
<tr>
<td align="center">

<div align="center">

**🚀 Ready to contribute?** Open an issue or submit a pull request!

</div>

---

## 📄 License

<div align="center">

This project is licensed under the **MIT License** 📜

*Feel free to use, modify, and share!*

</div>

---

## 🙏 Acknowledgments

<div align="center">

### 💖 **Special Thanks**

🐼 **Pandas Team** - For creating this amazing library
🐍 **Python Community** - For continuous support and innovation
📚 **Data Science Community** - For sharing knowledge and best practices
🎓 **Learners Like You** - For making this journey worthwhile

</div>

---

<div align="center">

## 🎉 Ready to Start?

### 🚀 **Begin Your Pandas Journey Today!**

<table>
<tr>
<td align="center">

---

### 💬 **Questions? Issues? Ideas?**

[💭 **Open an Issue**](https://github.com/KanekiEzz/Learn_Basic_Pandas_In_15_Qs/issues) | [📧 **Contact Us**](mailto:your-email@example.com) | [🌟 **Star this Repo**](https://github.com/KanekiEzz/Learn_Basic_Pandas_In_15_Qs)

---

**Happy Learning! 🐼✨**

*Transform your data manipulation skills with pandas!*

</div>
