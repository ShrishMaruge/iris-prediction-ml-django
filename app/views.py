from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

import pickle
import os
import numpy as np

base_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path=os.path.join(base_path,"model.pkl")

with open(model_path,"rb") as f:
    model=pickle.load(f)





def home(request):
    total=None
    if request.method == "POST":
        sl=request.POST.get("sl",0)
        sw=request.POST.get("sw",0)
        pl=request.POST.get("pl",0)
        pw=request.POST.get("pw",0)
        a=np.array([[float(sl),float(sw),float(pl),float(pw)]])
        prediction=model.predict(a)

        total=prediction[0]

    return render(request,"home.html",{"total": total})
    

        