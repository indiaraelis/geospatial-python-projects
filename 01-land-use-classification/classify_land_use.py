import rasterio
from rasterio.plot import show
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Load multispectral satellite image
with rasterio.open('satellite_image.tif') as src:
    img = src.read()
    profile = src.profile

# Prepare data (reshape for ML)
n_bands, height, width = img.shape
X = img.reshape(n_bands, height * width).T  # shape: (pixels, bands)

# Example labels (for demo purposes, normally from training data)
# Here, random labels are generated just for script completeness
y = np.random.randint(0, 3, size=height*width)

# Split data for training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train Random Forest Classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Predict and evaluate
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))

# Save classified image
classified = clf.predict(X).reshape(height, width)
with rasterio.open('classified_land_use.tif', 'w', **profile) as dst:
    dst.write(classified.astype(rasterio.uint8), 1)
