#  user_audit.py
"""
import and merge user lists from company systems to create
a master list of users and remove duplicates and orphans
"""

import pandas as pd
import glob


def read_ms365():
    ms = pd.read_csv("./downloads/user_list/ms.csv", usecols=["mail"])
    return ms


def read_r365():
    r365 = pd.read_csv(
        "./downloads/user_list/r365.csv",
        usecols=[
            "Full Name",
            "Username",
            "User Email",
            "Default Location",
            "User Roles",
            "Report Roles",
            "Active",
            "Created On",
            "Modified On",
        ],
    )
    r365 = r365.rename(columns={"User Email": "user_email"})
    r365 = r365[r365["Active"] == "Yes"]
    #    rackspace = pd.read_csv('./downloads/user_list/rackspace.csv')
    return r365


def read_rackspace():
    file_path = glob.glob("./downloads/user_list/rackspace/*.csv")
    dfs = [pd.read_csv(f) for f in file_path]
    rackspace = pd.concat(dfs, ignore_index=True)
    rackspace = rackspace.rename(columns={"Email": "user_email"})
    return rackspace


def read_reference():
    reference = pd.read_csv(
        "./downloads/user_list/centra_ref_users.csv",
        usecols=[
            "user_login",
            "user_email",
            "display_name",
            "ca_user_type",
        ],
    )
    return reference


def main(master, file, source):
    # merge user lists
    merged = pd.merge(
        master, file, how="outer", left_on=master["mail"].str.lower(), right_on=file["user_email"].str.lower()
    )

    in_master = merged.dropna(subset=["mail", "user_email"])
    not_in_master = merged[merged["mail"].isnull()]
    not_in_file = merged[merged["user_email"].isnull()]

    # export master user list
    print(in_master)
    input("Press Enter to continue...")
    print(not_in_master)
    input("Press Enter to continue...")
    print(not_in_file)
    input("Press Enter to continue...")
    # matches.to_csv("./output/user_list/users.csv", index=False)
    with pd.ExcelWriter(f"./output/user_list/{source}.xlsx") as writer:
        in_master.to_excel(writer, sheet_name="in_master", index=False)
        not_in_master.to_excel(writer, sheet_name="not_in_master", index=False)
        not_in_file.to_excel(writer, sheet_name="not_in_file", index=False)


if __name__ == "__main__":
    ms365 = read_ms365()

    r365 = read_r365()
    main(ms365, r365, "r365")
    rackspace = read_rackspace()
    main(ms365, rackspace, "rackspace")
    reference = read_reference()
    main(ms365, reference, "reference")
#    dashboard = read_dashboard()
