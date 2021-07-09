#Author: Eduardo Valverde

from bokeh.io import curdoc
from bokeh.layouts import column, layout
from bokeh.models import Button, CheckboxButtonGroup, RadioButtonGroup, Div, Slider, Dropdown, Select, Spacer
from afib.risk_scores import care, afriMale, afriFem, chad, poaf, npoaf

age = Slider(start=0, end=100, value=1, step=1, title="Age (y)")

care_div = Div(text="Care score: ", width=200, height=100)
afri_div = Div(text="Afri score: ", width=200, height=100)
chad_div = Div(text="Chad score: ", width=200, height=100)
poaf_div = Div(text="Poaf score: ", width=200, height=100)
npoaf_div = Div(text="Npoaf score: ", width=200, height=100)

menu = [("Stable cardiac disease, no other medical problems, undergoing noncomplex surgery","cd"), 
        ("Stable cardiac disease, one or more controlled medical problems, undergoing noncomplex surgery","cdmp"), 
        ("Any uncontrolled medical problem OR undergoing complex surgery","or"), 
        ("Any uncontrolled medical problem AND undergoing complex surgery","and"), 
        ("Chronic or advanced cardiac disease undergoing cardiac surgery as a last hope to save or improve life","lh")]

def careClick(careNum):
    if (careNum.item == "cd"):
        care_div.text = "Care score: " + str(care(True,False,False,False,False))
    elif(careNum.item == "cdmp"):
        care_div.text = "Care score: " + str(care(False,True,False,False,False))
    elif(careNum.item == "or"):
        care_div.text = "Care score: " + str(care(False,False,True,False,False))
    elif(careNum.item == "and"):
        care_div.text = "Care score: " + str(care(False,False,False,True,False))
    elif(careNum.item == "lh"):
        care_div.text = "Care score: " + str(care(False,False,False,False,True))

care_opt = Dropdown(label="Choose Description", menu=menu)
care_opt.on_click(careClick)

def afriUpd(attr, old, new):
    if (afri_sex.active == 0):
        if (afri_isPVD.active == [0, 2]):
            afri_div.text = "Afri score: " + str(afriMale(age.value, afri_wt.value, afri_ht.value, True))
        else:
            afri_div.text = "Afri score: " + str(afriMale(age.value, afri_wt.value, afri_ht.value, False))
    else:
        if (afri_isPVD.active == [0, 2]):
            afri_div.text = "Afri score: " + str(afriFem(age.value, afri_wt.value, afri_ht.value, True))
        else:
            afri_div.text = "Afri score: " + str(afriFem(age.value, afri_wt.value, afri_ht.value, False))

afri_wt = Slider(start=0, end=100, value=1, step=1, title="Weight (kg)")
afri_ht = Slider(start=0, end=250, value=1, step=1, title="Height (cm)")
afri_isPVD = CheckboxButtonGroup(labels=["Peripheral Vascular Disease?"], active=[2])
afri_sex = RadioButtonGroup(labels=["Male","Female"], active=0)
afri_wt.on_change('value',afriUpd)
afri_ht.on_change('value',afriUpd)
afri_isPVD.on_change('active',afriUpd)
afri_sex.on_change('active',afriUpd)

def updButton(button):
    if (button.active == [0,2]):
        return True
    else:
        return False

def chadUpd(attr, old, new):
    chad_div.text = "Chad score: " + str(chad(updButton(chad_chf),
                                          updButton(chad_htn),
                                          age.value,
                                          updButton(chad_dm),
                                          updButton(chad_stroke),
                                          updButton(chad_vd),
                                          updButton(chad_sex)))

chad_chf = CheckboxButtonGroup(labels=["Congestive Heart Failure?"], active=[2])
chad_htn = CheckboxButtonGroup(labels=["Hypertension?"], active=[2])
chad_dm = CheckboxButtonGroup(labels=["Diabetes Mellitus?"], active=[2])
chad_stroke = CheckboxButtonGroup(labels=["Stroke/TIA?"], active=[2])
chad_vd = CheckboxButtonGroup(labels=["Vascular Disease?"], active=[2])
chad_sex = CheckboxButtonGroup(labels=["Female?"], active=[2])
chad_chf.on_change('active',chadUpd)
chad_htn.on_change('active',chadUpd)
chad_dm.on_change('active',chadUpd)
chad_stroke.on_change('active',chadUpd)
chad_vd.on_change('active',chadUpd)
chad_sex.on_change('active',chadUpd)

def poafUpd(attr, old, new):
    poaf_div.text = "Poaf score: " + str(poaf(age.value,
                                          updButton(poaf_copd),
                                          poaf_egfr.value,
                                          updButton(poaf_emrgncy),
                                          updButton(poaf_pibp),
                                          (poaf_lvef.value/100),
                                          updButton(poaf_vs)))

poaf_copd = CheckboxButtonGroup(labels=["Chronic Obstructive Pulmonary Disease?"], active=[2])
poaf_egfr = Slider(start=0, end=120, value=1, step=1, title="Estimated Glomerular Filtration Rate")
poaf_emrgncy = CheckboxButtonGroup(labels=["Emergency?"], active=[2])
poaf_pibp = CheckboxButtonGroup(labels=["Preoperative Intra-aortic Balloon Pump?"], active=[2])
poaf_lvef = Slider(start=0, end=100, value=1, step=1, title="Left Ventricular Ejection Fraction (x/100)")
poaf_vs = CheckboxButtonGroup(labels=["Valve Surgery?"], active=[2])
poaf_copd.on_change('active', poafUpd)
poaf_egfr.on_change('value', poafUpd)
poaf_emrgncy.on_change('active', poafUpd)
poaf_pibp.on_change('active', poafUpd)
poaf_lvef.on_change('value', poafUpd)
poaf_vs.on_change('active', poafUpd)

def npoafUpd(attr, old, new):
    npoaf_div.text = "Npoaf score: " + str(npoaf(age.value,
                                            npoaf_mvd.value,
                                            updButton(npoaf_lad)))

mvd_menu = [("None","None"),("Mild","Mild"),("Moderate","Moderate"),("Severe","Severe")]
npoaf_mvd = Select(title="Mitrial Valve Disease Description:", value="None", options=["None", "Mild", "Moderate", "Severe"])
npoaf_lad = CheckboxButtonGroup(labels=["Left Atrial Dilatation?"], active=[2])
npoaf_mvd.on_change('value', npoafUpd)
npoaf_lad.on_change('active', npoafUpd)


age.on_change('value',afriUpd,chadUpd,poafUpd,npoafUpd)


afri_widgets = column(afri_wt,afri_ht,afri_isPVD,afri_sex)
chad_widgets = column(chad_chf,chad_htn,chad_dm,chad_stroke,chad_vd,chad_sex)
poaf_widgets = column(poaf_copd,poaf_egfr,poaf_emrgncy,poaf_pibp,poaf_lvef,poaf_vs)
npoaf_widgets = column(npoaf_mvd,npoaf_lad)

curdoc().add_root(layout(children=[
    [column(age)],
    [Spacer()],
    [column(care_opt), care_div],
    [Spacer()],
    [afri_widgets, afri_div],
    [Spacer()],
    [chad_widgets, chad_div],
    [Spacer()],
    [poaf_widgets, poaf_div],
    [Spacer()],
    [npoaf_widgets, npoaf_div]
], sizing_mode="stretch_height"))

"""
curdoc().add_root(column(care_opt,div,afri_age,afri_wt,afri_ht,afri_isPVD,afri_sex, div1))
curdoc().add_root(column(chad_chf,chad_htn,chad_age,chad_dm,chad_stroke,chad_vd,chad_sex,div2))
curdoc().add_root(column(poaf_age,poaf_copd,poaf_egfr,poaf_emrgncy,poaf_pibp,poaf_lvef,poaf_vs,div3))
curdoc().add_root(column(npoaf_age,npoaf_mvd,npoaf_lad,div4))
"""