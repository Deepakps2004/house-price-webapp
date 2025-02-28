from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_price(square_feet, num_rooms, quality):
    base_price_per_sqft = 2500
    quality_multiplier = {"Excellent": 1.3, "Very Good": 1.2, "Good": 1.1, "Average": 1.0}
    room_multiplier = 50000

    area = int(square_feet.split()[0])
    rooms = int(num_rooms.split()[0])
    quality_factor = quality_multiplier.get(quality, 1.0)

    return area * base_price_per_sqft * quality_factor + (rooms * room_multiplier)
houses = [
  {"square_feet": "1500 sq ft", "property_age": "5 years", "location": "Salem", "interior_exterior": "Modern", "num_rooms": "3 BHK", "quality": "Excellent", "image_url": "https://images.unsplash.com/photo-1568605114967-8130f3a36994", "contact": "+91-9876543210", "description": "Built with imported Italian marble and premium wood finishes."},
    {"square_feet": "1800 sq ft", "property_age": "8 years", "location": "Salem", "interior_exterior": "Classic", "num_rooms": "4 BHK", "quality": "Good", "image_url": "https://images.unsplash.com/photo-1572120360610-d971b9d7767c", "contact": "+91-9876543211", "description": "Features handcrafted tiles and custom teakwood doors."},
    {"square_feet": "1200 sq ft", "property_age": "3 years", "location": "Salem", "interior_exterior": "Minimalist", "num_rooms": "2 BHK", "quality": "Very Good", "image_url": "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9", "contact": "+91-9876543212", "description": "Designed with eco-friendly materials and modular interiors."},
    {"square_feet": "1600 sq ft", "property_age": "7 years", "location": "Salem", "interior_exterior": "Luxury", "num_rooms": "3 BHK", "quality": "Excellent", "image_url": "https://images.unsplash.com/photo-1598228723793-52759c8210da", "contact": "+91-9876543213", "description": "Furnished with exclusive granite flooring and imported fixtures."},
    {"square_feet": "1400 sq ft", "property_age": "4 years", "location": "Salem", "interior_exterior": "Traditional", "num_rooms": "3 BHK", "quality": "Very Good", "image_url": "https://images.unsplash.com/photo-1600585152935-7635cf40c13b", "contact": "+91-9876543214", "description": "Combines traditional design with modern conveniences."},
    {"square_feet": "2000 sq ft", "property_age": "10 years", "location": "Salem", "interior_exterior": "Rustic", "num_rooms": "5 BHK", "quality": "Excellent", "image_url": "https://images.unsplash.com/photo-1564013799919-ab600027ffc6", "contact": "+91-9876543215", "description": "Crafted using reclaimed wood and natural stone for timeless appeal."},
    {"square_feet": "1100 sq ft", "property_age": "2 years", "location": "Salem", "interior_exterior": "Modern", "num_rooms": "2 BHK", "quality": "Good", "image_url": "https://images.unsplash.com/photo-1573652636601-e1801545996d", "contact": "+91-9876543216", "description": "Smart home with energy-efficient fittings and chic design."},
    {"square_feet": "1500 sq ft", "property_age": "5 years", "location": "Salem", "interior_exterior": "Modern", "num_rooms": "3 BHK", "quality": "Excellent", "image_url": "https://images.unsplash.com/photo-1507089947368-19c1da9775ae", "description": "Designed with imported Italian marble and state-of-the-art fittings.", "contact": "98765 43210"},
    {"square_feet": "1800 sq ft", "property_age": "8 years", "location": "Salem", "interior_exterior": "Classic", "num_rooms": "4 BHK", "quality": "Good", "image_url": "https://images.unsplash.com/photo-1560185127-6a2e7b7a0e3b", "description": "Built using premium eco-friendly materials.", "contact": "98765 43211"},
    {"square_feet": "1200 sq ft", "property_age": "3 years", "location": "Salem", "interior_exterior": "Minimalist", "num_rooms": "2 BHK", "quality": "Very Good", "image_url": "https://images.unsplash.com/photo-1599423300746-b62533397364", "description": "Furnished with bespoke interiors and elegant lighting.", "contact": "98765 43212"},
    {"square_feet": "1600 sq ft", "property_age": "7 years", "location": "Salem", "interior_exterior": "Luxury", "num_rooms": "3 BHK", "quality": "Excellent", "image_url": "https://images.unsplash.com/photo-1600585152946-38b0b0e8a1f1", "description": "A perfect blend of contemporary design and heritage charm.", "contact": "98765 43213"},
    {"square_feet": "1400 sq ft", "property_age": "4 years", "location": "Salem", "interior_exterior": "Traditional", "num_rooms": "3 BHK", "quality": "Very Good", "image_url": "https://images.unsplash.com/photo-1600585152935-7635cf40c13b", "description": "Crafted with traditional woodwork and artisanal tiles.", "contact": "98765 43214"},
    {"square_feet": "2000 sq ft", "property_age": "10 years", "location": "Salem", "interior_exterior": "Rustic", "num_rooms": "5 BHK", "quality": "Excellent", "image_url": "https://images.unsplash.com/photo-1564013799919-ab600027ffc6", "description": "Charming farmhouse with vintage vibes.", "contact": "98765 43215"},
    {"square_feet": "1100 sq ft", "property_age": "2 years", "location": "Salem", "interior_exterior": "Modern", "num_rooms": "2 BHK", "quality": "Good", "image_url": "https://images.unsplash.com/photo-1573652636601-e1801545996d", "description": "Smart home with IoT automation.", "contact": "98765 43216"},
    {"square_feet": "1750 sq ft", "property_age": "6 years", "location": "Salem", "interior_exterior": "Bohemian", "num_rooms": "3 BHK", "quality": "Average", "image_url": "https://picsum.photos/400/300?random=8", "description": "Boho paradise with colorful decor.", "contact": "98765 43217"},
    {"square_feet": "1900 sq ft", "property_age": "9 years", "location": "Salem", "interior_exterior": "Industrial", "num_rooms": "4 BHK", "quality": "Very Good", "image_url": "https://picsum.photos/400/300?random=9", "description": "Exposed brick walls and steel accents.", "contact": "98765 43218"},
    {"square_feet": "1300 sq ft", "property_age": "3 years", "location": "Salem", "interior_exterior": "Contemporary", "num_rooms": "2 BHK", "quality": "Excellent", "image_url": "https://picsum.photos/400/300?random=10", "description": "Open plan living with custom cabinetry.", "contact": "98765 43219"},
    {"square_feet": "1250 sq ft", "property_age": "5 years", "location": "Salem", "interior_exterior": "Scandinavian", "num_rooms": "2 BHK", "quality": "Good", "image_url": "https://picsum.photos/400/300?random=11", "description": "Minimal design with maximum impact.", "contact": "98765 43220"},
    {"square_feet": "1850 sq ft", "property_age": "8 years", "location": "Salem", "interior_exterior": "Colonial", "num_rooms": "4 BHK", "quality": "Excellent", "image_url": "https://picsum.photos/400/300?random=12", "description": "Colonial charm meets modern comfort.", "contact": "98765 43221"},
    {"square_feet": "1700 sq ft", "property_age": "7 years", "location": "Salem", "interior_exterior": "Mediterranean", "num_rooms": "3 BHK", "quality": "Very Good", "image_url": "https://picsum.photos/400/300?random=13", "description": "Tiled roof, archways, and sunlit courtyards.", "contact": "98765 43222"},
    {"square_feet": "1550 sq ft", "property_age": "6 years", "location": "Salem", "interior_exterior": "Fusion", "num_rooms": "3 BHK", "quality": "Good", "image_url": "https://picsum.photos/400/300?random=14", "description": "Unique fusion of styles for eclectic taste.", "contact": "98765 43223"},
    {"square_feet": "1950 sq ft", "property_age": "10 years", "location": "Salem", "interior_exterior": "Victorian", "num_rooms": "5 BHK", "quality": "Excellent", "image_url": "https://picsum.photos/400/300?random=15", "description": "Victorian elegance with manicured gardens.", "contact": "98765 43224"},
    {"square_feet": "1400 sq ft", "property_age": "5 years", "location": "Salem", "interior_exterior": "Zen", "num_rooms": "3 BHK", "quality": "Very Good", "image_url": "https://picsum.photos/400/300?random=16", "description": "Calm vibes with indoor gardens.", "contact": "98765 43225"},
]


for house in houses:
    house["price"] = calculate_price(house["square_feet"], house["num_rooms"], house["quality"])

@app.route('/', methods=['GET', 'POST'])
def home():
    filtered_houses = houses[:]
    
    if request.method == 'POST':
        location = request.form.get('location')
        num_rooms = request.form.get('num_rooms')
        quality = request.form.get('quality')

        if location:
            filtered_houses = [house for house in filtered_houses if house['location'] == location]
        if num_rooms:
            filtered_houses = [house for house in filtered_houses if house['num_rooms'] == num_rooms]
        if quality:
            filtered_houses = [house for house in filtered_houses if house['quality'] == quality]

    sort_order = request.args.get('sort')
    if sort_order == "low-to-high":
        filtered_houses = sorted(filtered_houses, key=lambda x: x["price"])
    elif sort_order == "high-to-low":
        filtered_houses = sorted(filtered_houses, key=lambda x: x["price"], reverse=True)

    return render_template("index.html", houses=filtered_houses, selected_sort=sort_order)

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
