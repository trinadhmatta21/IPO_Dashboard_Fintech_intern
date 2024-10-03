# forms.py

from django import forms
from .models import IPO

class IPOForm(forms.ModelForm):
    class Meta:
        model = IPO
        fields = ['company_logo', 'company_name', 'price_band', 'open_date', 'close_date', 'issue_size', 'issue_type', 
                  'listing_date', 'status', 'ipo_price', 'listing_price', 'listing_gain', 'new_listing_date', 
                  'current_market_price', 'current_return', 'rhp_pdf', 'drhp_pdf']
