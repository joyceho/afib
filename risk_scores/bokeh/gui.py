from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models import Button, CheckboxButtonGroup, CustomJS, RadioButtonGroup, Div, Slider
from afib.risk_scores import care
from afib.risk_scores import afriMale, afriFem
from afib.risk_scores import chad

LABELS = ["cd", "cdmp", "or", "and", "lh"]

div = Div(text="Care score: ", width=200, height=100)
div1 = Div(text="Afri score: ", width=200, height=100)
div2 = Div(text="Chad score: ", width=200, height=100)

def careClick(careNum):
    if (careNum == 0):
        div.text = "Care score: " + str(care(True,False,False,False,False))
    elif(careNum == 1):
        div.text = "Care score: " + str(care(False,True,False,False,False))
    elif(careNum == 2):
        div.text = "Care score: " + str(care(False,False,True,False,False))
    elif(careNum == 3):
        div.text = "Care score: " + str(care(False,False,False,True,False))
    elif(careNum == 4):
        div.text = "Care score: " + str(care(False,False,False,False,True))

care_opt = RadioButtonGroup(labels=LABELS, active=5)
care_opt.on_click(careClick)

def afriUpd(attr, old, new):
    if (afri_sex.active == 0):
        if (afri_isPVD.active == [0, 2]):
            div1.text = "Afri score: " + str(afriMale(afri_age.value, afri_wt.value, afri_ht.value, True))
        else:
            div1.text = "Afri score: " + str(afriMale(afri_age.value, afri_wt.value, afri_ht.value, False))
    else:
        if (afri_isPVD.active == [0, 2]):
            div1.text = "Afri score: " + str(afriFem(afri_age.value, afri_wt.value, afri_ht.value, True))
        else:
            div1.text = "Afri score: " + str(afriFem(afri_age.value, afri_wt.value, afri_ht.value, False))

afri_age = Slider(start=0, end=100, value=1, step=1, title="Age (y)")
afri_wt = Slider(start=0, end=100, value=1, step=1, title="Weight (kg)")
afri_ht = Slider(start=0, end=250, value=1, step=1, title="Height (cm)")
afri_isPVD = CheckboxButtonGroup(labels=["Peripheral Vascular Disease?"], active=[2])
afri_sex = RadioButtonGroup(labels=["Male","Female"], active=0)
afri_age.on_change('value',afriUpd)
afri_wt.on_change('value',afriUpd)
afri_ht.on_change('value',afriUpd)
afri_isPVD.on_change('active',afriUpd)
afri_sex.on_change('active',afriUpd)

def chadUpd(attr, old, new):
    div2.text = "Chad score: " + str(chad())

chad_ = CheckboxButtonGroup(labels=["Peripheral Vascular Disease?"], active=[2])

curdoc().add_root(column(care_opt,div))
curdoc().add_root(column(afri_age,afri_wt,afri_ht,afri_isPVD,afri_sex, div1))