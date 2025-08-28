{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "8f5c008c-fbec-40ff-b5a9-797e410d8da4",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pyodbc\n",
    "\n",
    "def get_cursor():\n",
    "    conn = pyodbc.connect(\n",
    "        r\"Driver={ODBC Driver 17 for SQL Server};\"\n",
    "        r\"Server=localhost\\SQLEXPRESS;\"   # your instance\n",
    "        r\"Database=Python23;\"              # your database\n",
    "        r\"Trusted_Connection=yes;\"       # use Windows login\n",
    "    )\n",
    "    cursor = conn.cursor()\n",
    "    return cursor, conn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "66b9b393-f2a0-442b-bd4c-88992246310f",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
