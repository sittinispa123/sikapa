DISEASE_INFO = {
    "Anthracnose": {
        "description": "Penyakit daun yang ditandai bercak cokelat hingga cokelat tua dan kerusakan jaringan daun.",
        "solution": "Kurangi kelembapan berlebih, lakukan sanitasi, dan buang bagian daun yang mengalami kerusakan berat.",
        "handling": ["Periksa daun secara berkala.", "Pangkas dan buang bagian daun yang rusak berat.", "Jaga kebersihan dan sirkulasi udara kebun.", "Gunakan fungisida sesuai label dan rekomendasi petugas bila diperlukan."],
        "prevention": ["Gunakan bahan tanam sehat.", "Lakukan sanitasi kebun rutin.", "Hindari kondisi terlalu lembap.", "Lakukan pemantauan sejak gejala awal."]
    },
    "Curvularia": {
        "description": "Penyakit yang berkaitan dengan infeksi jamur dan dapat menimbulkan bercak pada permukaan daun.",
        "solution": "Kurangi kelembapan berlebih dan sumber inokulum melalui sanitasi serta pemangkasan bagian daun yang rusak.",
        "handling": ["Lakukan pemeriksaan daun secara berkala.", "Pangkas daun dengan kerusakan berat.", "Buang sisa daun terinfeksi dari kebun.", "Gunakan fungisida sesuai diagnosis dan rekomendasi teknis bila diperlukan."],
        "prevention": ["Gunakan bahan tanam sehat.", "Jaga kebersihan kebun.", "Perbaiki drainase dan sirkulasi udara.", "Pantau perkembangan bercak secara berkala."]
    },
    "Dryness": {
        "description": "Kondisi kekeringan pada daun yang dapat ditandai daun kering, layu, atau pencokelatan akibat cekaman air.",
        "solution": "Perbaiki pengelolaan air dan pertahankan kelembapan tanah sesuai kebutuhan tanaman.",
        "handling": ["Periksa kelembapan tanah.", "Pastikan tanaman memperoleh air yang cukup.", "Atur penyiraman sesuai kondisi lingkungan.", "Kendalikan gulma yang bersaing mendapatkan air."],
        "prevention": ["Kelola air secara teratur.", "Pertahankan kelembapan tanah.", "Kendalikan gulma.", "Pantau tanaman pada periode curah hujan rendah."]
    },
    "Fungal Disease": {
        "description": "Kelompok gejala penyakit yang berkaitan dengan infeksi jamur dan dapat menyebabkan bercak serta kerusakan jaringan daun.",
        "solution": "Lakukan sanitasi, kurangi kelembapan berlebih, dan kendalikan sumber infeksi secara dini.",
        "handling": ["Periksa daun secara berkala.", "Pangkas bagian yang rusak berat.", "Buang sisa tanaman terinfeksi.", "Gunakan fungisida sesuai diagnosis dan rekomendasi teknis bila diperlukan."],
        "prevention": ["Gunakan bahan tanam sehat.", "Lakukan sanitasi kebun.", "Hindari kelembapan berlebihan.", "Lakukan monitoring rutin."]
    },
    "Magnesium Deficiency": {
        "description": "Kondisi kekurangan magnesium yang dapat menyebabkan klorosis atau perubahan warna daun, terutama pada daun yang lebih tua.",
        "solution": "Evaluasi kesuburan tanah dan berikan sumber magnesium sesuai hasil analisis serta rekomendasi pemupukan.",
        "handling": ["Amati pola perubahan warna daun.", "Lakukan analisis tanah bila tersedia.", "Evaluasi program pemupukan.", "Berikan sumber magnesium sesuai rekomendasi teknis dan pantau perubahannya."],
        "prevention": ["Terapkan pemupukan berimbang.", "Lakukan analisis tanah secara berkala.", "Sesuaikan pemupukan dengan kebutuhan tanaman.", "Pantau kondisi daun secara rutin."]
    },
    "Serangan Apogonia": {
        "description": "Kerusakan daun akibat aktivitas hama pemakan daun yang dapat terlihat sebagai lubang atau bagian daun yang hilang.",
        "solution": "Lakukan monitoring populasi dan tingkat kerusakan serta gunakan pengendalian terpadu berdasarkan tingkat serangan.",
        "handling": ["Periksa tanaman secara rutin.", "Identifikasi keberadaan hama dan tingkat kerusakan.", "Jaga kebersihan area kebun.", "Gunakan pengendalian yang sesuai rekomendasi petugas bila diperlukan."],
        "prevention": ["Lakukan monitoring hama rutin.", "Jaga kebersihan kebun.", "Kendalikan gulma dan tanaman pengganggu.", "Terapkan pengendalian hama terpadu."]
    }
}

ALIASES = {
    "Antracnose": "Anthracnose", "Anthracnose": "Anthracnose",
    "Culvaria": "Curvularia", "Curvularia": "Curvularia",
    "Dryness": "Dryness", "Fungal Disease": "Fungal Disease",
    "Magnesium Deficiency": "Magnesium Deficiency",
    "Serangan Apogonia": "Serangan Apogonia"
}

def normalize_disease_name(name):
    return ALIASES.get(str(name).strip(), str(name).strip())
