# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuration
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

print("VISUALISATION DES RESULTATS - Mini DataLake")


# 1. VENTES PAR PAYS
print("\n1. Chargement: Ventes par pays...")
try:
    df_country = pd.read_csv('results/sales_by_country.csv')
    print(f"   Lignes: {len(df_country)}")
    print("\nTop 10 pays par revenus:")
    print(df_country.head(10).to_string(index=False))
    
    # Graphique
    plt.figure(figsize=(12, 6))
    top10_countries = df_country.head(10)
    plt.barh(top10_countries['COUNTRY'], top10_countries['TOTAL_SALES'])
    plt.xlabel('Revenus Total ($)')
    plt.ylabel('Pays')
    plt.title('Top 10 Pays par Revenus')
    plt.tight_layout()
    plt.savefig('results/chart_sales_by_country.png', dpi=300)
    print("\n   ✓ Graphique sauvegarde: results/chart_sales_by_country.png")
    plt.close()
    
except Exception as e:
    print(f"   Erreur: {e}")

# 2. TOP PRODUITS
print("\n2. Chargement: Top produits...")
try:
    df_products = pd.read_csv('results/top_products.csv')
    print(f"   Lignes: {len(df_products)}")
    print("\nCategories de produits:")
    print(df_products.to_string(index=False))
    
    # Graphique
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Quantite
    ax1.bar(df_products['PRODUCTLINE'], df_products['TOTAL_QUANTITY'])
    ax1.set_xlabel('Categorie')
    ax1.set_ylabel('Quantite Vendue')
    ax1.set_title('Quantites Vendues par Categorie')
    ax1.tick_params(axis='x', rotation=45)
    
    # Revenus
    ax2.bar(df_products['PRODUCTLINE'], df_products['TOTAL_REVENUE'], color='green')
    ax2.set_xlabel('Categorie')
    ax2.set_ylabel('Revenus ($)')
    ax2.set_title('Revenus par Categorie')
    ax2.tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.savefig('results/chart_top_products.png', dpi=300)
    print("\n   ✓ Graphique sauvegarde: results/chart_top_products.png")
    plt.close()
    
except Exception as e:
    print(f"   Erreur: {e}")

# 3. VENTES PAR TRIMESTRE
print("\n3. Chargement: Ventes par trimestre...")
try:
    df_quarter = pd.read_csv('results/sales_by_quarter.csv')
    print(f"   Lignes: {len(df_quarter)}")
    print("\nVentes par trimestre:")
    print(df_quarter.to_string(index=False))
    
    # Graphique
    df_quarter['PERIOD'] = df_quarter['YEAR_ID'].astype(str) + '-Q' + df_quarter['QTR_ID'].astype(str)
    plt.figure(figsize=(12, 6))
    plt.plot(df_quarter['PERIOD'], df_quarter['TOTAL_SALES'], marker='o', linewidth=2)
    plt.xlabel('Periode')
    plt.ylabel('Ventes ($)')
    plt.title('Evolution des Ventes par Trimestre')
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('results/chart_sales_by_quarter.png', dpi=300)
    print("\n   ✓ Graphique sauvegarde: results/chart_sales_by_quarter.png")
    plt.close()
    
except Exception as e:
    print(f"   Erreur: {e}")

# 4. TOP CLIENTS
print("\n4. Chargement: Top clients...")
try:
    df_customers = pd.read_csv('results/top_customers.csv')
    print(f"   Lignes: {len(df_customers)}")
    print("\nTop 10 clients:")
    print(df_customers.head(10).to_string(index=False))
    
    # Graphique
    plt.figure(figsize=(12, 8))
    top10_customers = df_customers.head(10)
    plt.barh(range(len(top10_customers)), top10_customers['TOTAL_SPENT'])
    plt.yticks(range(len(top10_customers)), 
               [f"{row['CUSTOMERNAME'][:30]}\n({row['COUNTRY']})" 
                for _, row in top10_customers.iterrows()])
    plt.xlabel('Depenses Totales ($)')
    plt.title('Top 10 Clients par Depenses')
    plt.tight_layout()
    plt.savefig('results/chart_top_customers.png', dpi=300)
    print("\n   ✓ Graphique sauvegarde: results/chart_top_customers.png")
    plt.close()
    
except Exception as e:
    print(f"   Erreur: {e}")

# 5. STATISTIQUES GLOBALES
print("\n5. Statistiques globales:")
try:
    total_revenue = df_country['TOTAL_SALES'].sum()
    total_orders = df_country['NB_ORDERS'].sum()
    avg_order = total_revenue / total_orders if total_orders > 0 else 0
    
    print(f"\n   • Revenu total: ${total_revenue:,.2f}")
    print(f"   • Commandes totales: {total_orders:,}")
    print(f"   • Valeur moyenne commande: ${avg_order:,.2f}")
    print(f"   • Nombre de pays: {len(df_country)}")
    print(f"   • Nombre de produits: {len(df_products)}")
    
except Exception as e:
    print(f"   Erreur: {e}")

print("VISUALISATION TERMINEE !")
