api_response = [
    {
        "candidate": "Alice",
        "history": {"jobs": ["Data Analyst", "Data Scientist"]}
    },
    {
        "candidate": "Bob",
        "history": {"jobs": ["Recruiter"]}
    }
]

def flattened_data(data):
  flat_data = []
  for record in data:
    name = record["candidate"]
    job_list = record["history"]["jobs"]
    for job in job_list:
      flat_record = {
        "candidate_name":name,
        "job_list":job
      }
    flat_data.append(flat_record)
  
  return flat_data;


print(flattened_data(api_response));