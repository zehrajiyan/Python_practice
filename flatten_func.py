def flatten_list(nested):
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten_list(item))  # iç içe listeyse yine aynı fonksiyonu çağır
        else:
            result.append(item)
    return result