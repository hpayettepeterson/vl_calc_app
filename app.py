import streamlit as st

st.markdown("""# How much could you save with [VisioLab](https://visiolab.io/)?
## Calculate your estimated yearly savings...
""")

# button for more info
if st.button('What counts as one point of sale?'):
    st.write('A point of sale is a checkout (normally with one cashier) where one person can pay for their food at a time')

st.markdown("""------------------
## How many points of sale do you have?
""")
pos = st.slider('', 1, 20, 3)

st.write('Your points of sale: ', pos)



#@st.cache

def calc_cashier_number(pos):
    # minimum 1 cashier, at least 1 cashier per 4 VL units
    cashiers = ((pos - 1) // 4 + 1)
    vl = pos - cashiers
    return cashiers, vl

cashiers = calc_cashier_number(pos)[0]
vl = calc_cashier_number(pos)[1]

def calc_savings(pos, cashiers, vl, c_cost_yearly=27000, vl_cost_monthly=400):
    # c_cost_yearly: cashier yearly salary in euros
    # vl_cost_monthly: VL system cost in euros
    vl_cost_yearly = vl_cost_monthly * 12
    # total cost with no VL systems
    cost_without_vl = pos * c_cost_yearly
    # total cost with max number of VL systems
    cost_with_vl = (c_cost_yearly * cashiers) + (vl_cost_yearly * vl)
    # yearly money saved by using VL systems
    savings = cost_without_vl - cost_with_vl
    return savings

savings = calc_savings(pos, cashiers, vl, c_cost_yearly=270000, vl_cost_monthly=400)

st.markdown("""
## Keeping the same number of points of sale, your canteen setup would look like this:
""")
st.write('Number of cashiers: ', cashiers)
st.write('Number of VL systems: ', vl)

st.markdown("""
## Your estimated yearly savings would be:
""")
st.write(savings, 'Euros')

st.markdown("""\n
            \n
            \n
            \n
            \n
            ----------------------------------
            """)

# button for more info
if st.button('More info...'):
    st.write(
        'At least one cashier is needed per 4 VisioLab units, to help customers with the process (a bit like automated checkouts in supermarkets).'
    )
    st.write(
        'This is calculated assuming an average yearly salary of 27000 Euros per cashier.')



# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slider


# and used in order to select the displayed lines
