applicants = ["alice@test.com", "bob@test.com", "charlie@test.com"]
hired = ["bob@test.com"]

def find_rejected_applicants(applicants_list, hired_list):
    applicants_set = set(applicants_list)
    hired_set = set(hired_list)
    
    rejected = applicants_set - hired_set
    
    return list(rejected)


print(find_rejected_applicants(applicants, hired))