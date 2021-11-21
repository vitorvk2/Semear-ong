import 'package:flutter/material.dart';
import 'package:semear/components/oficina_item.dart';
import 'package:semear/pages/home/home.service.dart';
import 'package:semear/pages/pesquisa/pesquisa.service.dart';

class PesquisaPage extends StatefulWidget {
  @override
  _PesquisaPageState createState() => _PesquisaPageState();
}

class _PesquisaPageState extends State<PesquisaPage> {
  void forceReload() {
    setState(() {});
  }

  void getSubscribedOficinas() async {
    List<dynamic> oficinas = await getOficinas();

    for (var i = 0; i < oficinas.length; i++) {
      oficinasSubscribed.add(oficinas[i]['id']);
    }
  }

  @override
  void initState() {
    super.initState();

    getSubscribedOficinas();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: SingleChildScrollView(
          child: Padding(
            padding: EdgeInsets.all(30),
            child: Column(
              children: [
                Container(
                  width: MediaQuery.of(context).size.width,
                  margin: EdgeInsets.only(bottom: 40),
                  child: Row(
                    children: [
                      IconButton(
                        padding: EdgeInsets.zero,
                        onPressed: () {
                          Navigator.of(context).pop();
                        },
                        icon: Icon(
                          Icons.arrow_back_outlined,
                          color: Colors.black,
                          size: 35,
                        ),
                        alignment: Alignment.centerLeft,
                        color: Colors.blue,
                      ),
                      Text(
                        'Pesquisa',
                        style: TextStyle(
                          fontSize: 30,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ],
                  ),
                ),
                Container(
                  child: TextField(
                    controller: searchController,
                    onChanged: (e) {
                      onChangeSearch(e, forceReload);
                    },
                    decoration: InputDecoration(
                      hintText: "Pesquise",
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.all(Radius.circular(8)),
                      ),
                    ),
                  ),
                ),
                Container(
                  margin: EdgeInsets.only(top: 20),
                  child: ListView.builder(
                    physics: NeverScrollableScrollPhysics(),
                    primary: true,
                    shrinkWrap: true,
                    itemCount: oficinasSearch.length,
                    itemBuilder: (BuildContext ctx, int i) {
                      return OficinaItemComponent(
                        oficina: oficinasSearch[i],
                        isSubscribed: oficinasSubscribed.contains(
                          oficinasSearch[i]['id'],
                        ),
                      );
                    },
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
