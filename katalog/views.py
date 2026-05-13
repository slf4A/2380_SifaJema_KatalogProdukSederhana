from django.shortcuts import render

produk_list = [
    {
        'id': 1,
        'nama': 'Laptop',
        'harga': 'Rp 8.000.000',
        'deskripsi': 'Laptop untuk belajar dan kerja',
        'gambar': 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?q=80&w=800'
    },
    {
        'id': 2,
        'nama': 'Mouse',
        'harga': 'Rp 150.000',
        'deskripsi': 'Mouse wireless',
        'gambar': 'https://images.unsplash.com/photo-1527814050087-3793815479db?q=80&w=800'
    },
    {
        'id': 3,
        'nama': 'Keyboard',
        'harga': 'Rp 300.000',
        'deskripsi': 'Keyboard mechanical',
        'gambar': 'https://images.unsplash.com/photo-1511467687858-23d96c32e4ae?q=80&w=800'
    },
    {
        'id': 4,
        'nama': 'Headphone',
        'harga': 'Rp 500.000',
        'deskripsi': 'Headphone dengan kualitas suara jernih',
        'gambar': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?q=80&w=800'
    },
    {
        'id': 5,
        'nama': 'Smartphone',
        'harga': 'Rp 4.500.000',
        'deskripsi': 'Smartphone modern dengan kamera HD',
        'gambar': 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?q=80&w=800'
    },
]

# Homepage
def home(request):
    return render(request, 'katalog/home.html')

# Daftar produk
def produk(request):
    return render(request, 'katalog/produk.html', {
        'produk': produk_list
    })

# Detail produk
def detail_produk(request, id):
    produk_detail = None

    for item in produk_list:
        if item['id'] == id:
            produk_detail = item

    return render(request, 'katalog/detail_produk.html', {
        'produk': produk_detail
    })

# Kontak
def kontak(request):
    return render(request, 'katalog/kontak.html')
