import 'package:flutter/material.dart';
import 'package:semear/components/bootom_menu.dart';
import 'package:semear/components/fomatter_datetime.dart';

import 'chamada.service.dart';

class ChamadaPage extends StatefulWidget {
  final int oficinaId;

  ChamadaPage({required this.oficinaId});

  @override
  _ChamadaPageState createState() => _ChamadaPageState();
}

class _ChamadaPageState extends State<ChamadaPage> {
  List<dynamic> chamadas = [];

  void getApiChamadas() async {
    chamadas = await getFaltas(widget.oficinaId);
    setState(() {});
  }

  @override
  void initState() {
    super.initState();
    getApiChamadas();
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
                        'Suas faltas',
                        style: TextStyle(
                          fontSize: 30,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ],
                  ),
                ),
                ListView.builder(
                  primary: true,
                  shrinkWrap: true,
                  physics: NeverScrollableScrollPhysics(),
                  itemBuilder: (BuildContext ctx, int index) {
                    return ListTile(
                      leading: FormatterDateTimeComponent(
                        date: chamadas[index]['created_at'],
                        style: TextStyle(fontSize: 17),
                      ),
                      trailing: Text(
                        !chamadas[index]['presente'] ? "Ausente" : "Presente",
                        style: TextStyle(
                          color: !chamadas[index]['presente']
                              ? Colors.redAccent
                              : Colors.black,
                          fontSize: 17,
                        ),
                      ),
                    );
                  },
                  itemCount: chamadas.length,
                ),
              ],
            ),
          ),
        ),
      ),
      bottomNavigationBar: BottomMenuComponent(),
    );
  }
}
