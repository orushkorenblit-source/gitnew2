# gitnew2 — דשבורד אינטרקטיבי

אפליקציית ווב אינטרקטיבית לבחינת נתוני Iris באמצעות גרף פיזור (scatter plot) דינמי. המשתמש בוחר את צירי X ו-Y מתוך רשימה, והגרף מתעדכן בזמן אמת.

## תכונות

- בחירת משתנים לציר X ולציר Y מתוך עמודות מספריות בנתונים
- גרף פיזור צבוע לפי מין הפרח (`species`)
- ממשק בעברית

## דרישות

- Python 3.8 ומעלה
- החבילות: `dash`, `plotly`, `pandas`

## התקנה

```bash
git clone https://github.com/orushkorenblit-source/gitnew2.git
cd gitnew2
pip install dash plotly pandas
```

או עם קובץ דרישות (אם תוסיף `requirements.txt`):

```bash
pip install -r requirements.txt
```

## הרצה

```bash
python test.py
```

לאחר ההרצה, פתח בדפדפן את הכתובת שמוצגת בטרמינל (בדרך כלל `http://127.0.0.1:8050`).

## מבנה הפרויקט

```
gitnew2/
├── test.py      # אפליקציית Dash הראשית
└── README.md
```

## טכנולוגיות

| רכיב | שימוש |
|------|--------|
| [Dash](https://dash.plotly.com/) | מסגרת לאפליקציית הווב |
| [Plotly Express](https://plotly.com/python/plotly-express/) | יצירת הגרפים |
| [Pandas](https://pandas.pydata.org/) | עבודה עם טבלאות נתונים |

נתוני הדוגמה מגיעים ממערך הנתונים המובנה `px.data.iris()` של Plotly.

## רישיון

לא הוגדר רישיון בפרויקט. הוסף קובץ `LICENSE` לפי הצורך.
