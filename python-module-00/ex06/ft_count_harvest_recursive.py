def ft_count_harvest_recursive(day, max_days) -> None:
    if day > max_days:
        return
    print("Day ", day)
    ft_count_harvest_recursive(day + 1, max_days)


days = int(input("Days until harvest: "))
# ft_count_harvest_recursive(1, days)
