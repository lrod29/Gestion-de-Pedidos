def importe_total_carro(request):
    total = 0
    if request.user.is_authenticated:
        carro = request.session.get('carro', {})
        for item in carro.values():
            total += float(item['precio']) 
    return {'importe_total_carro': total}

