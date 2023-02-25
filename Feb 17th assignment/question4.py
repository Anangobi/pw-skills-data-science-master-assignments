data1={"Name":"gobianan",
       "college":"sns college of technology",
       "dept":"Information technology"
}
data12=[{"Name":"gobianan",
       "college":"sns college of technology",
       "dept":"Information technology"
},{"Name":"suriya",
       "college":"sns college of technology",
       "dept":"Information technology"
},{"Name":"parasuraman",
       "college":"sns college of technology",
       "dept":"Information technology"
},{"Name":"aadish",
       "college":"sns college of technology",
       "dept":"Information technology"
},{"Name":"gayathri",
       "college":"sns college of technology",
       "dept":"Information technology"
}]
col_gobi.insert_one(data1)
col_gobi.insert_many(data12)
for i in col_gobi.find({'Name':"gobianan"}):
    print(i)
for i in col_gobi.find_one({'Name':"gobianan"}):
    print(i)
