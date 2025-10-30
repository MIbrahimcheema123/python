student_data = {
    "id1":
    {
        "name":"Ibrahim",
        "grade":8,
        "subject":"English,Math,Science"
        },
    "id2":
    {
        "name":"Hamza",
        "grade":7,
        "subject":"English,Math,Science"
},  "id3":
{
        "name":"Abdullah",
        "grade":6,
        "subject":"English,Math,Science"
}," id4":
{
        "name":"Ibrahim",
        "grade":8,
        "subject":"English,Math,Science"
        },
}
result = {}
for key,value in student_data.items():
    if value not in result.values():
        result[key] = value
print(result)