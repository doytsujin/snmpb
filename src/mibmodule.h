/**
 * Copyright (c) 2004-2017 Martin Jolicoeur and contributors
 *
 * This file is part of the snmpb project and is free software: you can
 * redistribute it and/or modify it under the terms of the GNU General
 * Public License as published by the Free Software Foundation, either
 * version 3 of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#ifndef MIBMODULE_H
#define MIBMODULE_H

#include <smi.h>

#include "snmpb.h"
#include "mibview.h"

#define PATH_SEPARATOR ';'

class LoadedMibModule
{
public:
    LoadedMibModule(SmiModule* mod);
    
    void PrintProperties(QString& text);   
    char* GetMibLanguage(void);

    QString name;
    SmiModule *module;
};

class MibModule: public QObject
{
    Q_OBJECT
    
public:
    enum AutomaticLoadingPolicy {MIBLOAD_ALL, MIBLOAD_DEFAULT, MIBLOAD_NONE};

    MibModule(Snmpb *snmpb);
    void Refresh(void);
    void RefreshPathChange(void);
    void SendLogError(const QString& text){ErrorWhileLoading=true; emit LogError(text);}
    QString LoadBestModule(QString oid);
    void SetLoadingPolicy(enum AutomaticLoadingPolicy p) {Policy = p;}

public slots:
    void AddModule(void);
    void RemoveModule(void);
    void ShowModuleInfo(void);

signals:
    void ModuleProperties(const QString& text);
    void LogError(const QString& text);
    void StopAgentTimer(void);

private:
    void InitLib(int restart);
    void RebuildTotalList(int restart);
    void RebuildLoadedList(void);
    void RebuildUnloadedList(void);
    void SaveWantedModules(void);

private:
    Snmpb *s;

    QStringList Unloaded;
    QList<LoadedMibModule*> Loaded;
    QList<QStringList> Total;
    QStringList Wanted;
    enum AutomaticLoadingPolicy Policy;
    bool ErrorWhileLoading;
};

#endif /* MIBMODULE_H */
