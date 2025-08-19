{
    
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "fbbba060",
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "import numpy as np\n",
    "\n",
    "img = cv2.imread(\"img2.png\")\n",
    "gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)\n",
    "edges = cv2.Canny(gray,75,150)\n",
    "\n",
    "lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50)\n",
    "\n",
    "for line in lines:\n",
    "    x1, y1, x2, y2 = line[0]\n",
    "    cv2.line(img, (x1,y1), (x2,y2), (0,255,0), 3)\n",
    "\n",
    "cv2.imshow(\"edges\", edges)\n",
    "cv2.imshow(\"Image\", img)\n",
    "cv2.waitKey(0)\n",
    "cv2.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None, 
   "id": "a497723c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
