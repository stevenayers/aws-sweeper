def display_results(resource_type, results):
    if results:
        print(resource_type + 'found')
    else:
        print('No potentially unwanted or unused ' + resource_type + ' were found.')
